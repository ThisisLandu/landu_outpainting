import math, cv2, random, torch, torchvision
import numpy as np
import nodes


def normalize_size_base_64(w, h):
    short_side = min(w, h)
    remainder = short_side % 64
    return short_side - remainder + (64 if remainder > 0 else 0)


class Pad_Image:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mode_type": (
                    [
                        "Top-Left",
                        "Top",
                        "Top-Right",
                        "Center-Left",
                        "Center",
                        "Center-Right",
                        "Bottom-Left",
                        "Bottom",
                        "Bottom-Right",
                        "Random",
                    ],
                ),
                "Ratio_min": ("FLOAT", {"default": 0.5, "min": 0.3, "max": 2.0, "step": 0.1, "round": 0.01, "dispaly": "slider"}),
                "Ratio_max": ("FLOAT", {"default": 0.7, "min": 0.5, "max": 2.0, "step": 0.1, "round": 0.01, "dispaly": "slider"}),
                "pad_mode": (["constant", "replicate", "noise"],),
            },
        }

    RETURN_TYPES = (
        "IMAGE",
        # "MASK",
        "IMAGE",
    )
    RETURN_NAMES = (
        "image",
        # "masks",
        "pose_image",
    )

    FUNCTION = "run"

    # OUTPUT_NODE = False

    CATEGORY = "Landu"

    def run(self, image, mode_type, pad_mode, Ratio_min, Ratio_max):  # image= 1,768,512,3
        obj = nodes.NODE_CLASS_MAPPINGS["DWPreprocessor"]()
        resolution = normalize_size_base_64(image.shape[2], image.shape[1])
        pose_image = obj.estimate_pose(image, True, True, True, resolution=resolution)["result"][0]
        print("pose iamge shape", pose_image.shape)
        print(pose_image.max(), image.max())

        Resize_by = random.uniform(Ratio_min, Ratio_max)
        if Resize_by > 0.9999 and Resize_by < 1.0001:
            return image
        x, y = int(image.shape[2] * Resize_by), int(image.shape[1] * Resize_by)
        resized_image = torchvision.transforms.Resize((y, x))(image.permute(0, 3, 1, 2))  # 1,3,768,512
        dx, dy = abs(image.shape[2] - resized_image.shape[3]), abs(image.shape[1] - resized_image.shape[2])
        rdx, rdy = random.randint(0, dx), random.randint(0, dy)
        if Resize_by < 1:
            mode_list = {
                "Top-Left": (0, dx, 0, dy),
                "Top": (int(dx / 2), int(dx / 2) + 1, 0, dy),
                "Top-Right": (dx, 0, 0, dy),
                "Center-Left": (0, dx, int(dy / 2), int(dy / 2)),
                "Center": (int(dx / 2), int(dx / 2) + 1, int(dy / 2), int(dy / 2)),
                "Center-Right": (dx, 0, int(dy / 2), int(dy / 2)),
                "Bottom-Left": (0, dx, dy, 0),
                "Bottom": (int(dx / 2), int(dx / 2) + 1, dy, 0),
                "Bottom-Right": (dx, 0, dy, 0),
                "Random": (rdx, dx - rdx, rdy, dy - rdy),
            }
            padded_image = torch.rand_like(image.permute(0, 3, 1, 2))
            if pad_mode == "noise":
                padded_image[
                    :,
                    :,
                    mode_list[mode_type][2] : padded_image.shape[2] - mode_list[mode_type][3],
                    mode_list[mode_type][0] : padded_image.shape[3] - mode_list[mode_type][1],
                ] = resized_image
                padded_image = padded_image.permute(0, 2, 3, 1)
            else:
                padded_image = torch.nn.functional.pad(resized_image, (mode_list[mode_type]), mode=pad_mode).permute(0, 2, 3, 1)
        elif Resize_by > 1:
            o_h, o_w = image.shape[1], image.shape[2]
            r_h, r_w = resized_image.shape[2], resized_image.shape[3]
            mode_list = {
                "Top-Left": (0, o_w, 0, o_h),
                "Top": (int(dx / 2), o_w + int(dx / 2), 0, o_h),
                "Top-Right": (dx, r_w, 0, o_h),
                "Center-Left": (0, o_w, int(dy / 2), o_h + int(dy / 2)),
                "Center": (int(dx / 2), o_w + int(dx / 2), int(dy / 2), o_h + int(dy / 2)),
                "Center-Right": (dx, r_w, int(dy / 2), o_h + int(dy / 2)),
                "Bottom-Left": (0, o_w, dy, r_h),
                "Bottom": (int(dx / 2), o_w + int(dx / 2), dy, r_h),
                "Bottom-Right": (dx, r_w, dy, r_h),
                "Random": (rdx, o_w + rdx, rdy, o_h + rdy),
            }
            padded_image = torch.rand_like(image.permute(0, 3, 1, 2))  # 1,3,768,512
            padded_image = resized_image[
                :,
                :,
                mode_list[mode_type][2] : mode_list[mode_type][3],
                mode_list[mode_type][0] : mode_list[mode_type][1],
            ]  # TODO 여기 코드짜면 됨 (resized가 더큼)
            padded_image = padded_image.permute(0, 2, 3, 1)
        # mask = torch.ones_like(padded_image[:, :, :, :1]) * 255  #
        # mask[
        #     :, mode_list[mode_type][2] : mask.shape[1] - mode_list[mode_type][3], mode_list[mode_type][0] : mask.shape[2] - mode_list[mode_type][1], :
        # ] = 0
        return (
            padded_image,
            # mask,
            pose_image,
        )


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {"Landu_Padding Image": Pad_Image}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {"Landu_Padding Image": "Landu_Padding Image"}

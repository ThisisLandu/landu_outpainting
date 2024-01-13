from .outpainting_node import *
from .wildcardencoder import *
from .save_image import *
from .set_queue import *
from .lowrise import *
from .non_switch import *

NODE_CLASS_MAPPINGS = {
    "Landu_Padding Image": Pad_Image,
    "Landu_Padding Image2": Pad_Image_v2,
    "Landu_ImpactWildcardEncode": Landu_ImpactWildcardEncode,
    "Landu_Ksampler": Landu_KSampler,
    "Landu_ToBasicPipe": Landu_ToBasicPipe,
    "Landu_FromBasicPipe_v2": Landu_FromBasicPipe_v2,
    "Landu_setimageinfo": Landu_setimageinfo,
    "Landu_SaveImage":Landu_SaveImage,
    "Landu_ImpactWildcardEncode_GetPrompt":Landu_ImpactWildcardEncode_GetPrompt,
    "Landu_SetQueue":Landu_SetQueue,
    "Landu_drawmask":Landu_drawmask,
    "Landu_FirstNonNull":Landu_FirstNonNull,
    "Landu_blendimages":Landu_blendimages,
    "Landu_blend_onecolor":Landu_blend_onecolor,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Landu_Padding Image": "Landu_Padding Image",
    "Landu_Padding Image2": "Landu_Padding Image2",
    "Landu_ImpactWildcardEncode": "Landu_ImpactWildcardEncode",
    "Landu_Ksampler": "Landu_Ksampler",
    "Landu_ToBasicPipe": "Landu_ToBasicPipe",
    "Landu_FromBasicPipe_v2": "Landu_FromBasicPipe_v2",
    "Landu_setimageinfo": "Landu_setimageinfo",
    "Landu_SaveImage" : "Landu_SaveImage",
    "Landu_ImpactWildcardEncode_GetPrompt":"Landu_ImpactWildcardEncode_GetPrompt",
    "Landu_SetQueue":"Landu_SetQueue",
    "Landu_drawmask":"Landu_drawmask",
    "Landu_FirstNonNull":"Landu_FirstNonNull",
    "Landu_blendimages":"Landu_blendimages",
    "Landu_blend_onecolor":"Landu_blend_onecolor",
}

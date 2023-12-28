from .outpainting_node import *
from .wildcardencoder import *

NODE_CLASS_MAPPINGS = {
    "Landu_Padding Image": Pad_Image,
    "Landu_Padding Image2": Pad_Image_v2,
    "Landu_ImpactWildcardEncode": Landu_ImpactWildcardEncode,
    "Landu_Ksampler": Landu_KSampler,
    "Landu_ToBasicPipe": Landu_ToBasicPipe,
    "Landu_FromBasicPipe_v2": Landu_FromBasicPipe_v2,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Landu_Padding Image": "Landu_Padding Image",
    "Landu_Padding Image2": "Landu_Padding Image2",
    "Landu_ImpactWildcardEncode": "Landu_ImpactWildcardEncode",
    "Landu_Ksampler": "Landu_Ksampler",
    "Landu_ToBasicPipe": "Landu_ToBasicPipe",
    "Landu_FromBasicPipe_v2": "Landu_FromBasicPipe_v2",
}

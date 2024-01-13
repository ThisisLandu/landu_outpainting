import random

basic_prompt = "__shortcut/basic_prompt1__, "
basic_prompt = "__shortcut/basic_prompt2__, "


id_list1 = [
    "__shortcut/a-haneul__, ",  #

    "__shortcut/a-chunmomo__, ",  # AD
    "__shortcut/a-glasses__, ",  # AD
    "__shortcut/a-nayeon__, ",  #
    "__shortcut/a-richae__, ",  #

    "__shortcut/a-olz__, ",  #
    "__shortcut/a-crimm__, ",  #

    "__shortcut/a-winter__, ",  #
    "__shortcut/a-haniminji__, ",  #
    "__shortcut/a-erika__, ",  #
    # '__shortcut/a-yuna__, ', #
    # "__shortcut/a-zinzalim__, ",  #
]


id_list2 = [
    "__shortcut/b-coco__, ",  #

    "__shortcut/b-yujeong__, ",  #
    "__shortcut/b-karina__, ",  #
    "__shortcut/b-momo__, ",  #
    "__shortcut/b-iu__, ",  #
    "__shortcut/b-eunbi__, ",  #
    "__shortcut/b-sana__, ",  #
    "__shortcut/b-gte__, ",  #
    # "__shortcut/b-lanan__, ",  #
    # "__shortcut/b-princess__, ",  #
    # "__shortcut/b-kodol__, ",  #
]

id_list4 = ["__shortcut/d-minju__, "]

breast_prompt1 = [" (flat chest:", "(small breast:"]
breast_prompt3 = [" (large breast:"]


def generate_rand(min=1.2, max=1.4, digit=2):
    return round(random.uniform(min, max), digit)


def load_txt(type):
    prompts = []
    with open(f"F:/image/StableDiffusion/prompt_generator/prompt_{type}.txt", "r") as file:
        for line in file:
            line = line.strip()  # 줄의 양 끝에 있는 공백 및 개행 문자 제거
            if line:  # 공백이 아닌 줄인 경우에만 리스트에 추가
                prompts.append(line)
    return prompts


def set_clothes(prom):
    cleavage = f"{{(cleavage:{generate_rand(0.5,1.2)})||}}"
    prom = (
        prom
        + f"{{:{generate_rand(1.2,1.4)})|:{generate_rand(0.9,1.0)}), (nude:{generate_rand(0.7,1.3)}), (NSFW:{generate_rand(1.1,1.4)})}},{cleavage} "
    )
    return prom


hair_accessory = ["pin", "clip", "barrette", "band", "tie", "elastic", "scrunchie", "bow", "ribbon", "hair_accessory"]
hair_color = ["gold", "white", "pink", "green", "blue", "red", "purple", "light blue", "brown", "black", "gray"]


# { | } 갯수 0개부터~ 확률 randint(0,2)=0,1,2
# 100%, 50%, 33%, 25%, 20%, 16.6%, 14%, 12.5%, 11.1% , 10%
def add_detail(prom, args, prob=0.1):
    if random.random() < prob:
        if args == "head_access":
            if random.random() < 0.8:  # 헤어장식 등장확률
                choice = "hair " + random.choice(hair_accessory)
            else:
                choice = random.choice(["cat", "rabbit"]) + " ear"
            prom.append(f"{{({choice}:{generate_rand(1.2,1.4)}), {'|' * random.randint(0,2)}}},  ")  # 100% ~ 33%
        if args == "hair_color":
            prom.append(f"({random.choice(hair_color)} hair:{generate_rand(1.2,1.4)}),  ")
        if args == "earring":
            prom.append(f"{{(earring:{generate_rand(1.0,1.3)}), {'|' * random.randint(0,2)}}},  ")  # 100% ~ 33%
        if args == "choker":
            prom.append(f"{{(choker:1.2), {'|' * random.randint(0,2)}}},  ")  # 100% ~ 33%
        if args == "smile":
            prom.append(f"{{(smile, smile512:{generate_rand(0.7,1.4)}), {'|' * random.randint(4,6)} }}, ")  # 20% ~ 14%
        if args == "blush":
            prom.append(f"{{(blush: {generate_rand(1.1,1.4)}), {'|' * random.randint(0,2)}}}, ")  # 100% ~ 33%
        if args == "camera":
            prom.append(
                f"{{({{POV|{{2$$from {{front|side|behind}}|from {{below|above}}|}}}}:{generate_rand(1.2,1.35)}), {'|' * random.randint(0,2)}}}, "
            )
        if args == "camera2":
            prom.append(f"{{({{face close up|cowboy shot|knee|feet}}:{generate_rand(1.1,1.35)}), {'|' * random.randint(3,5)}}}, ")
        if args == "camera3":
            prom.append(f"{{(pectoral focus:1.5, chest macro shot:1.4), {'|' * random.randint(3,4)}}}, ")  # 25% ~ 20%
        if args == "fisheye":
            prom.append(f"{{(fisheye_lens_angle:{generate_rand(1.3,1.6)}) {'|' * random.randint(2,3)}}}, ")  # 33% ~ 25%
        if args == "theme":
            prom.append(f"({random.choice(hair_color)} theme:1.3), ")
        if args == "light":
            prom.append(f"backlighting,<lora:backlighting:{generate_rand(0.05,0.5)}>,  ")
        if args == "night":
            prom.append(f"dark theme,  <lora:LowRA:0.6>,  (midnight:{generate_rand(1.2,1.4)}),  ")

    return prom

(prompts_tagger, prompts_complete, prompts_place, prompts_hair, prompts_clothes, prompts_gpt) = (
    load_txt("tagger"),
    load_txt("complete"),
    load_txt("place"),
    load_txt("hair"),
    load_txt("clothes"),
    load_txt("gpt"),
)




def make_prompt(mode,etc):
    id_list,breast_prompt=[],[]
    prom = []

    prob = random.random()
    if prob < 0.0:  # 완성프롬
        prom.append(random.choice(prompts_complete))

    elif prob < 0.3:  # Tagger
        prom_tagger = random.choice(prompts_tagger)
        prom.append(
            f"({prom_tagger.strip().split('BREAK')[0]}:{{1.3), |0.6), (nude,NSFW:1.3), cleavage, {random.choice(['<lora:GoodPussyV1:0.6>,','',''])} }}, {prom_tagger.strip().split('BREAK')[1]} "
        )
    elif prob < 0.6:  # gpt
        prom_gpt = random.choice(prompts_gpt)
        prom.append(f"{prom_gpt}, {{(NSFW,nude:1.4|)}}, ")
        prom = add_detail(prom, "hair_color", 0.3)
        prom = add_detail(prom, "head_access", 0.2)
        prom = add_detail(prom, "earring", 0.4)
        prom = add_detail(prom, "camera", 0.5)
        prom = add_detail(prom, "camera2", 0.4)
    else:  # 만들기
        prom.append(f"({random.choice(prompts_place).strip()}:1.2), ")  # 장소 강화
        prom.append(f"({random.choice(prompts_hair).strip()}:1.2), ")  # 헤어 강화
        prom.append(set_clothes("(" + random.choice(prompts_clothes).strip()))  # 의상 강화
        if random.random() < 0.3:
            prom[0] = "(blank background:1.4), "  # 배경 무지배경으로
        elif random.random() < 0.1:
            prom.append(f"({random.choice(hair_color)} background:1.2), ")
            prom = add_detail(prom, "hair_color", 0.1)
            prom = add_detail(prom, "head_access", 0.2)
            prom = add_detail(prom, "earring", 0.4)
            prom = add_detail(prom, "camera", 0.8)
            prom = add_detail(prom, "camera2", 0.4)

    prom = add_detail(prom, "camera3", 0.5)  # 가슴확대 포즈
    prom = add_detail(prom, "fisheye", 0.05)  # 어안렌즈
    prom = add_detail(prom, "smile", 0.6)
    prom = add_detail(prom, "choker", 0.7)
    prom = add_detail(prom, "blush", 0.4)
    prom = add_detail(prom, "theme", 0.3)
    prom = add_detail(prom, "light", 0.4)
    prom = add_detail(prom, "night", 0.05)
    prom.append("(1girl:1.2), ")


    if mode=='ab':
        if etc %2 ==0:
            id_list=id_list1
            breast_prompt=breast_prompt1
        elif etc %2 ==1:
            id_list=id_list2
            breast_prompt=breast_prompt3
    elif mode=='d':
        id_list=id_list4
        breast_prompt=breast_prompt3
    prompt = f'{basic_prompt}{random.choice(id_list)}{random.choice(breast_prompt)}{generate_rand(1.2,1.4,1)}), BREAK\n {"".join(prom)}'

    return prompt
import numpy as np
from PIL import Image
from time import sleep
from urllib.request import urlopen
from .system import Clear

all_fonts = ['3-d', '3x5', '5lineoblique', '1943____', '4x4_offr', '64f1____', 'a_zooloo', 'advenger', 'aquaplan', 'asc_____', 'ascii___', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'b_m__200', 'battle_s', 'battlesh', 'baz__bil', 'beer_pub', 'bubble__', 'bubble_b', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'coil_cop', 'com_sen_', 'computer', 'convoy__', 'd_dragon', 'dcs_bfmo', 'deep_str', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'druid___', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'finalass', 'fireing_', 'flyn_sh', 'fp1_____', 'fp2_____', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'gauntlet', 'ghost_bo', 'gothic', 'gothic__', 'grand_pr', 'green_be', 'hades___', 'heavy_me', 'heroboti', 'high_noo', 'hills___', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'italics_', 'joust___', 'kgames_i', 'kik_star', 'krak_out', 'lazy_jon', 'letter_w', 'letterw3', 'magic_ma>', 'master_o', 'mayhem_d', 'mcg_____', 'mig_ally', 'modern__', 'new_asci', 'nfi1____', 'notie_ca', 'npn_____', 'odel_lak', 'ok_beer_', 'outrun__', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'panther_', 'pawn_ins', 'phonix__', 'platoon2', 'platoon_', 'pod_____', 'r2-d2___', 'rad_____', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'rally_sp', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'script__', 'skate_ro', 'skateord', 'skateroc', 'sketch_s', 'sm______', 'space_op', 'spc_demo', 'star_war', 'stealth_', 'stencil1', 'stencil2', 'street_s', 'subteran', 'super_te', 't__of_ap', 'tav1____', 'taxi____', 'tec1____', 'tec_7000', 'tecrvs__', 'ti_pan__', 'timesofl', 'tomahawk', 'top_duck', 'trashman', 'triad_st', 'ts1_____', 'tsm_____', 'tsn_base', 'twin_cob', 'type_set', 'ucf_fan_', 'ugalympi', 'unarmed_', 'usa_____', 'usa_pq__', 'vortron_', 'war_of_w', 'yie-ar__', 'yie_ar_k', 'z-pilot_', 'zig_zag_', 'zone7___', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D', 'banner3',
             'banner4', 'barbwire', 'basic', '5x7', '5x8', '6x10', '6x9', 'brite', 'briteb', 'britebi', 'britei', 'chartr', 'chartri', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'cour', 'courb', 'courbi', 'couri', 'helv', 'helvb', 'helvbi', 'helvi', 'sans', 'sansb', 'sansbi', 'sansi', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'times', 'tty', 'ttyb', 'utopia', 'utopiab', 'utopiabi', 'utopiai', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xsbooki', 'xtimes', 'xtty', 'xttyb', 'bell', 'big', 'bigchief', 'binary', 'block', 'broadway', 'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'contessa', 'contrast', 'cosmic', 'cosmike', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'decimal', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'dwhistled', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fraktur', 'goofy', 'graceful', 'gradient', 'graffiti', 'hex', 'hollywood', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'l4me', 'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow', 'mshebrew210', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'nvscript', 'o8', 'octal', 'ogre', 'os2', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief', 'relief2', 'rev', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'speed', 'stacey', 'stampatello', 'standard', 'starwars', 'stellar', 'stop', 'straight', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'weird', 'whimsy']

# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
complexGrayScale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,"^`\'. '

# 10 levels of gray
easyGrayScale = '@%#*+=-:. '


def getAverageColor(image: Image) -> object:
    '''
    Given PIL Image, return average value of grayscale color
    '''

    im = np.array(image)

    w, h = im.shape

    return np.average(im.reshape(w*h))


def img2ascii(file: str, width: int = 70, scale: float = 0.43, moreLevels: bool = False) -> str:

    if width < 1:
        raise ValueError("Width must be greater than 0.")

    if scale <= 0:
        raise ValueError("Scale must be greater than 0.")

    image = Image.open(file).convert('L')
    imgWidth, imgHeight = image.size

    columns = imgWidth//width
    ratio = columns/scale
    height = int(imgHeight//ratio)

    if width > imgWidth or height > imgHeight:
        return 'Image too small for specified size!'

    asciiArray = [''] * height

    for j in range(height):
        y1, y2 = int(j*ratio), int((j+1)*ratio)

        if j == height-1:
            y2 = imgHeight

        for i in range(width):
            x1, x2 = i*columns, (i+1)*columns

            if i == width-1:
                x2 = imgWidth

            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageColor(img))

            if moreLevels:
                gsval = complexGrayScale[(avg*len(complexGrayScale))//255]

            else:
                gsval = easyGrayScale[(avg*len(easyGrayScale))//255]

            asciiArray[j] += gsval

    return '\n'.join(asciiArray)


def font(font: str, text: str) -> str:
    if font not in all_fonts:
        return 'Error, Font not Found!'

    text = text.replace(' ', '+')

    api = 'https://artii.herokuapp.com/make?font={}&text={}'.format(font, text)
    asciiart = urlopen(api).read().decode('utf-8')

    return asciiart


def fonts_list(text: str = None) -> str:
    Clear()
    result = ''

    if not text:
        text = 'zelow'

    else:
        text = text.replace(' ', '+')

    for _font in all_fonts:
        try:
            api = f'https://artii.herokuapp.com/make?font={_font}&text={text}'
            asciiart = urlopen(api).read().decode('utf-8')
            result_one = 'name of the font >>> ' + _font + '\n' + asciiart + ':\n\n'
            result += result_one
            print(result_one)

        except:
            sleep(0.1)

        input()
        Clear()

    return result

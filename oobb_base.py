from oobb_get_items_base import *
import oobb
import os
import json
#import oomB

# base functions



def get_default_thing(**kwargs):

    thing = {}

    type_dict = {}
    type_dict.update({"bc": "bearing circle"})
    type_dict.update({"bp": "bearing plate"})
    type_dict.update({"bpj": "bearing plate with jack"})
    type_dict.update({"bpjb": "bearing plate with jack basic"})
    type_dict.update({"bw": "bearing wheel"})
    type_dict.update({"ci": "circle"})
    type_dict.update({"hl": "holder"})
    type_dict.update({"jab": "jack basic"})
    type_dict.update({"ja": "jack"})
    type_dict.update({"jg": "jig"})
    type_dict.update({"mps": "mounting plate single sided holes"})
    type_dict.update({"mpt": "mounting plate top and bottom holes"})
    type_dict.update({"mpu": "mounting plate u holes"})
    type_dict.update({"mp": "mounting plate"})
    type_dict.update({"pl": "plate"})
    type_dict.update({"tr": "tray"})
    
    type_dict.update({"sc": "shaft coupler"})
    type_dict.update({"sh": "shaft"})
    type_dict.update({"sj": "soldering jig"})
    type_dict.update({"th": "tool holder"})
    type_dict.update({"wh": "wheel"})
    type_dict.update({"wi": "wire plate"})
    type_dict.update({"ztj": "zip tie mount jack"})
    type_dict.update({"zt": "zip tie mount"})

    type_dict.update({"bearing": "bearing"})
    type_dict.update({"nut": "nut"})
    type_dict.update({"screw": "screw"})
    type_dict.update({"screw_countersunk": "screw countersunk"})
    type_dict.update({"screw_socket_cap": "screw socket cap"})
    type_dict.update({"standoff": "standoff"})
    type_dict.update({"threaded_insert": "threaded insert"})
    type_dict.update({"test": "test"})
    type_dict.update({"washer": "washer"})
    type_dict.update({"bolt": "bolt"})

    type = kwargs["type"]
    width = kwargs.get("width", "0")
    height = kwargs.get("height", "0")
    thickness = kwargs.get("thickness", "0")
    for key in type_dict:
        if type.startswith(key):
            thing.update(
                {"description": f"{type_dict[key]} {width}x{height}x{thickness}"})
    if thing.get("description", "") == "":
        thing.update({"description": f"{type_dict[type]}"})

    var_names = ["type", "width", "height", "diameter", "thickness", "radius_name", "depth",
                 "radius_hole", "width_mounting", "name", "bearing_name", "bearing_type", "oring_type","extra","shaft"]
    zfill_values = ["width", "height", "thickness", "depth", "diameter"]
    acronyms = {"width": "", "height": "", "diameter": "", "thickness": "", "depth": "", "size": "", "type": "", "radius_hole": "rh","radius_name": "", "width_mounting": "mo", "height_mounting": "hm","name": "nm", "bearing_name": "", "bearing_type": "","oring_type":"or", "extra":"ex", "shaft": "sh"}

    if type == "test":
        var_names.append("radius_name")
        acronyms.update({"radius_name": "rn"})
        var_names.append("shape")
        acronyms.update({"shape": "sh"})
        var_names.append("style")
        acronyms.update({"style": "st"})

    


    deets = {}
    for var in var_names:
        deets[var] = {}

        # if zfill
        if var in zfill_values:
            val = kwargs.get(var, "")
            if val != "":
                deets[var].update({"value": str(kwargs.get(var, "")).zfill(2)})
            else:
                deets[var].update({"value": kwargs.get(var, "")})
        else:
            deets[var].update({"value": kwargs.get(var, "")})
        deets[var].update({"acronym": acronyms[var]})
        if deets[var]["acronym"] != "":
            deets[var]["str"] = f"_{deets[var]['acronym']}_{deets[var]['value']}"
        else:
            deets[var]["str"] = f"_{deets[var]['value']}"

    id = kwargs.get("size", "")
    for var in deets:
        if deets[var]["value"] != "":
            if deets[var]["value"] != "":
                id += deets[var]["str"]
    id = id.replace(".","d")
    print(id)
    thing.update({"id": id})
    thing.update({"type": f"{type}"})
    try:
        thing.update({"type_oobb": f"{type_dict[type]}"})
    except:
        pass

    for var in var_names:
        try:
            thing.update({var: kwargs[var]})
        except:
            pass
    try:
        thing.update(
            {"width_mm": kwargs["width"] * ob.gv("osp") - ob.gv("osp_minus")})
    except:
        pass
    try:
        if thickness != "":
            thing.update({"thickness_mm": kwargs["thickness"]})
    except:
        pass
    try:
        thing.update(
            {"height_mm": kwargs["height"] * ob.gv("osp") - ob.gv("osp_minus")})
    except:
        pass
    thing.update({"components": []})

    return thing


def set_variable(name, value, mode=""):
    if mode != "":
        name = name + "_" + mode
    oobb.variables.update({name: value})


def gv(name, mode=""):
    return get_variable(name, mode)


def get_variable(name, mode=""):
    if mode != "":
        name = name + "_" + mode
    rv = oobb.variables[name]
    # print(f'{name} {rv}')
    return rv


def get_hole_pos(x, y, wid, hei, size="oobb"):
    sp = gv("osp")
    if size == "oobe":
        sp = gv("osp")/2
        

    x_mm = -(wid-1) * sp / 2 + (x - 1) * sp
    y_mm = -(hei-1) * sp / 2 + (y - 1) * sp
    return x_mm, y_mm


def add_thing(thing):
    oobb.things.update({thing["id"]: thing})


def dump(mode="json"):
    if mode == "json":
        with open('things.json', 'w') as outfile:
            json.dump(oobb.things, outfile)
        with open('variables.json', 'w') as outfile:
            json.dump(oobb.variables, outfile)
    elif mode == "folder":
        for thing in oobb.things:
            filename = f'things/{thing}/details.json'
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            with open(filename, 'w') as outfile:
                json.dump(oobb.things[thing], outfile, indent=4)


def load(mode="json"):
    if mode == "json":
        with open('things.json') as json_file:
            oobb.things = json.load(json_file)
        with open('variables.json') as json_file:
            variables = json.load(json_file)
    elif mode == "folder":
        # load all the details.json files from the fodlers in things directory
        for thing in os.listdir("things"):
            try:
                with open(f'things/{thing}/details.json') as json_file:
                    oobb.things.update({thing: json.load(json_file)})
            except FileNotFoundError:
                pass


def build_things(save_type="none", overwrite=True, filter=""):
    #turn filter into an array if its a string
    if type(filter) == str:
        filter = [filter]
    for f in filter:
        for thing in oobb.things:
            if f in thing:
                print(f'building {thing}')
                build_thing(thing, save_type, overwrite)


def build_thing(thing, save_type="all", overwrite=True):
    modes = ["3dpr", "laser", "true"]
    for mode in modes:
        depth = oobb.things[thing].get(
            "depth_mm", oobb.things[thing].get("thickness_mm", 3))
        height = oobb.things[thing].get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        opsc.opsc_make_object(f'things/{thing}/{mode}.scad', oobb.things[thing]["components"], mode=mode,
                              save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)

def build_thing_filename(thing, save_type="all", overwrite=True, filename="", depth=3, height = 200):
    modes = ["3dpr", "laser", "true"]
    for mode in modes:
        depth = depth
        height = height
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        opsc.opsc_make_object(f'{filename}{mode}.scad', thing, mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)



def oe(**kwargs):
    return oobb_easy(**kwargs)


def oobb_easy(**kwargs):
    try:
        kwargs["type"] = kwargs["t"]
        del kwargs["t"]
    except KeyError:
        pass
    try:
        kwargs["shape"] = kwargs["s"]
        del kwargs["s"]
    except KeyError:
        pass
    try:
        kwargs["radius_name"] = kwargs["rn"]
        del kwargs["rn"]
    except KeyError:
        pass

    if "oobb" in kwargs["shape"] or "oobe" in kwargs["shape"]:
        # if its an oobb_plat then call get_oobb_plate
        shape = kwargs["shape"]
        if shape == "oobb_pl":
            return_value = []
            holes = kwargs.get("holes", True)
            return_value.append(get_oobb_plate(**kwargs))
            if holes:
                return_value.extend(get_oobb_holes(**kwargs))
            return return_value
        if shape == "oobe_pl":
            return_value = []
            return_value.append(get_oobe_plate(**kwargs))
            return_value.extend(get_oobe_holes(**kwargs))
            return return_value
        else:
            # Call the function dynamically using its string name
            func = globals()[f'get_{shape}']
            return func(**kwargs)
    else:
        return opsc.opsc_easy(**kwargs)


def oobb_easy_array(**kwargs):
    for i in range(0, 3):
        kwargs["repeats"].append(1)
        kwargs["pos_start"].append(0)
        kwargs["shift_arr"].append(0)
    return_objects = []

    repeats = kwargs["repeats"]
    for x in range(0, repeats[0]):
        for y in range(0, repeats[1]):
            for z in range(0, repeats[2]):
                pos = [0, 0, 0]
                pos[0] = kwargs["pos_start"][0]+x*kwargs["shift_arr"][0]
                pos[1] = kwargs["pos_start"][1]+y*kwargs["shift_arr"][1]
                pos[2] = kwargs["pos_start"][2]+z*kwargs["shift_arr"][2]
                kwargs.update({"pos": pos})
                return_objects.append(oobb_easy(**kwargs))
    return return_objects


#shifting routines
def shift(thing,shift):
    # iterate through by index
    for i in range(0,len(thing)):
        component = thing[i]
        component = copy.deepcopy(component)
        thing[i] = component
        component["pos"][0] += shift[0]
        component["pos"][1] += shift[1]
        component["pos"][2] += shift[2]
    return thing

def highlight(thing):
    add_all(thing,"m","#")
    return thing

def remove_if(thing, name, value):
    thing2 = copy.deepcopy(thing)
    for component in thing2:
        if component.get(name,"") == value:
            thing.remove(component)
    return thing

def add_all(thing, name, value):
    for component in thing:
        component.update({name: value})
    return thing

def inclusion(thing, include):    
    thing2 = []
    for component in thing:
        inclusion = component.get("inclusion", "all")
        if include in inclusion or inclusion == "all":
            component["inclusion"] = include
            thing2.append(component)
            pass
        else:
            pass
    return thing






######### convenience functions #########

def get_oobb_hole_with_text(**kwargs):
    
    depth = kwargs.get("depth", 3)
    radius = kwargs.get("radius", 1)
    #offset_text = kwargs.get("offset_text", -10)
    offset_text = -radius - 1
    font_size = kwargs.get("font_size", 14)
    pos = kwargs.get("pos", [0, 0, 0])
    kwargs["pos"] = pos
    return_value = []
    p2 = copy.deepcopy(kwargs)
    return_value.extend(get_oobb_hole(**kwargs))
    p2 = copy.deepcopy(kwargs)
    p2["pos"][0] = p2["pos"][0] + offset_text 
    #shift z up by depth
    height_extrusion = 0.3
    p2["pos"][2] = p2["pos"][2] + depth - height_extrusion
    p2["height"] = height_extrusion
    p2["m"] = "#"
    #set halign center and valign center
    p2["halign"] = "right"
    p2["valign"] = "center"
    # deja vu sans mono as font
    p2["font"] = "DejaVu Sans Mono"
    #size equals font size
    p2["size"] = font_size
    return_value.extend(get_oobb_text(**p2))

    return return_value
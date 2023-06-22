from oobb_get_items_base import *
import oobb_base as ob


def get_bolt(**kwargs):
    wid = kwargs["radius_name"]
    depth = kwargs["depth"]
    thing = ob.get_default_thing(**kwargs)
    thing.update({"description": f"bolt {wid}x{depth}"})
    thing.update({"depth_mm": depth})

    thing.update({"components": []})
    thing["components"].extend(ob.oe(
        t="positive", s="oobb_bolt", rn=wid, depth=depth, rotY=0, include_nut=False))

    return thing


def get_nut_m3():
    nut = get_nut(3)
    return nut


def get_nut(**kwargs):

    wid = kwargs["radius_name"]

    thing = ob.get_default_thing(**kwargs)
    width = ob.gv(f"nut_radius_{wid}_true")
    depth = ob.gv(f"nut_depth_{wid}_true")
    thing.update({"description": f"nut {wid}x{depth}"})
    thing.update({"width_mm": width})
    thing.update({"depth_mm": depth})
    thing.update({"height_mm": width/1.154})

    th = thing["components"]
    th.extend(ob.oe(t="p", s="oobb_nut", rn=wid))
    th.extend(ob.oe(t="n", s="oobb_hole", rn=wid, depth=100, z=-10, m=""))

    return thing


def get_screw_countersunk(**kwargs):
    wid = kwargs["radius_name"]
    depth = kwargs["depth"]
    thing = ob.get_default_thing(**kwargs)
    thing.update({"description": f"screw countersunk {wid}x{depth}"})
    thing.update({"depth_mm": depth})

    thing.update({"components": []})
    thing["components"].extend(ob.oe(
        t="positive", s="oobb_countersunk", rn=wid, depth=depth, include_nut=False))

    return thing


def get_screw_socket_cap(**kwargs):
    wid = kwargs["radius_name"]
    depth = kwargs["depth"]
    thing = ob.get_default_thing(**kwargs)
    thing.update({"description": f"screw socket cap {wid}x{depth}"})
    thing.update({"depth_mm": depth})

    thing.update({"components": []})
    thing["components"].extend(ob.oe(
        t="positive", s="oobb_screw_socket_cap", rn=wid, depth=depth, include_nut=False))

    return thing


def get_standoff(**kwargs):

    wid = kwargs["radius_name"]
    depth = kwargs["depth"]
    thing = ob.get_default_thing(**kwargs)
    width = ob.gv(f"nut_radius_{wid}_true")

    thing.update({"description": f"standoff {wid}x{depth}x{depth}"})
    thing.update({"width_mm": width})
    thing.update({"depth_mm": depth})
    thing.update({"height_mm": width/1.154})

    th = thing["components"]
    th.extend(ob.oe(t="p", s="oobb_standoff", rn=wid, hole=True, depth=depth))
    # th.extend(ob.oe(t="n",s="oobb_hole", rn=wid,depth=100,z=-10,m=""))

    return thing


def get_threaded_insert(**kwargs):

    wid = kwargs["radius_name"]
    style = kwargs.get("style", "01")
    thing = ob.get_default_thing(**kwargs)
    width = ob.gv(f"threaded_insert_{style}_radius_{wid}_true")
    depth = ob.gv(f"threaded_insert_{style}_depth_{wid}_true")
    thing.update({"description": f"threaded insert {wid}x{depth}"})
    thing.update({"width_mm": width})
    thing.update({"depth_mm": depth})

    th = thing["components"]
    th.extend(ob.oe(t="p", s="oobb_threaded_insert", rn=wid, hole=False))
    th.extend(ob.oe(t="n", s="oobb_hole", rn=wid, depth=100, z=-10, m=""))

    return thing


def get_bearing(**kwargs):
    bearing_name = kwargs["bearing_name"]
    thing = ob.get_default_thing(**kwargs)
    thing.update({"description": f"bearing {bearing_name}"})

    th = thing["components"]
    th.extend(ob.oe(t="positive", s="oobb_cylinder",
              radius_name=f'bearing_{bearing_name}_od', depth=f"bearing_{bearing_name}_depth"))
    th.extend(ob.oe(t="negative", s="oobb_cylinder",
              radius_name=f'bearing_{bearing_name}_id', depth=f"bearing_{bearing_name}_depth"))

    return thing

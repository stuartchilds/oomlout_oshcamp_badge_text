
#import oobb_get_items_oobb
import oobb_get_items_other
import oobb_get_items_base
import oobb_get_items_oobb
import oobb_get_items_test
import oobb_base


def make_all(filter=""):
    # typs = ["bps","jas","mps","pls","nuts","screws_countersunk","tests","zts"]
    # add orings make a nice summary page maybe tables of details add 2020 maybe
    typs = ["bps", "bcs", "cis", "hls", "jas", "jgs", "mps", "pls", "scs",
             "shs", "sjs", "ths", "trs", "zts", "nuts", "wis", "whs", "screws", "bearings", "nuts", "tests"]
   
    all_things = []

    for type in typs:
        if filter in type:
            func = globals()["get_"+type]
            all_things.extend(func())
            pass

    for thing in all_things:
        try:
            func = getattr(oobb_get_items_oobb, "get_"+thing["type"])
        except AttributeError:
            try:
                func = getattr(oobb_get_items_other, "get_"+thing["type"])
            except:
                func = getattr(oobb_get_items_test, "get_"+thing["type"])

        thing = func(**thing)
        oobb_base.add_thing(thing)
        pass


# oobb makes

def get_bps(size="oobb"):
    bps = []
    bps.append({"type": "bp", "width": 3, "height": 3, "thickness": 12, "bearing_type": "606","size": size})
    bps.append({"type": "bpj", "width": 3, "height": 3, "thickness": 12, "bearing_type": "606","size": size})
    bps.append({"type": "bpjb", "width": 3, "height": 3, "thickness": 12, "bearing_type": "606","size": size})
    bps.append({"type": "bp", "width": 3, "height": 3, "thickness": 12, "bearing_type": "6704","size": size})
    bps.append({"type": "bp_shim", "thickness": 2, "bearing_type": "6704", "size": size})
    bps.append({"type": "bp", "width": 3, "height": 3, "thickness": 12, "bearing_type": "6704", "size": size, "shaft": "motor_gearmotor_01"})
    bps.append({"type": "bp", "width": 3, "height": 3, "thickness": 12, "bearing_type": "6704", "size": size, "shaft": "motor_servo_micro_01"})
    bps.append({"type": "bp", "width": 3, "height": 3, "thickness": 12, "bearing_type": "6803", "size": size})
    bps.append({"type": "bp", "width": 3, "height": 3, "thickness": 12, "bearing_type": "6804", "size": size})
    bps.append({"type": "bp", "width": 5, "height": 5, "thickness": 12, "bearing_type": "6808", "size": size})
    bps.append({"type": "bp", "width": 7, "height": 5, "thickness": 12, "bearing_type": "6810", "size": size})

    return bps

def get_bcs(size="oobb"):
    bcs = []
    bcs.append({"type": "bc", "diameter": 3, "thickness": 12, "bearing_type": "606","size": size})

    return bcs



def get_cis(size="oobb"):
    circles = []
    circle_size = [1.5,3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    for s in circle_size:
        circles.append({"type": "ci", "diameter": s, "thickness": 3, "size": size})
    
    circles.append({"type": "ci", "diameter": 1.5, "thickness": 12, "extra":"nut_m6", "size": size})


    circles.append({"type": "ci_cap", "diameter": 3, "thickness": 9, "shaft":"electronics_potentiometer_17", "size": size})
    circles.append({"type": "ci_cap", "diameter": 1.5, "thickness": 6, "shaft":"electronics_potentiometer_17", "size": size})
    
    circles.append({"type": "ci_cap", "diameter": 3, "thickness": 9, "shaft":"motor_gearmotor_01", "size": size})
    circles.append({"type": "ci_cap", "diameter": 1.5, "thickness": 9, "shaft":"motor_gearmotor_01", "size": size})

    return circles


def get_hls(size="oobb"):
    hls = []
    #### gearmotor
    hls.append({"type": "hl", "extra": "motor_gearmotor_01","width": 6, "height": 3, "thickness": 6, "size": size})
    #### micro servo
    hls.append({"type": "hl", "extra": "motor_servo_micro_01","width": 4, "height": 3, "thickness": 3, "size": size})
    
    #### nema 17
    thicknesses = [3,6]
    for t in thicknesses:
        ##shifted nema 17s    
        hls.append({"type": "hl", "extra": "motor_stepper_motor_nema_17_flat","width": 5, "height": 3, 
        "thickness": t, "size": size, "bearing_type": "shifted"})
        hls.append({"type": "hl", "extra": "motor_stepper_motor_nema_17_flat","width": 5, "height": 5, 
        "thickness": t, "size": size, "bearing_type": "shifted"})
        ##normal nema 17s
        hls.append({"type": "hl", "extra": "motor_stepper_motor_nema_17_flat","width": 5, "height": 3, 
        "thickness": t, "size": size})
        hls.append({"type": "hl", "extra": "motor_stepper_motor_nema_17_flat","width": 5, "height": 5, 
        "thickness": t, "size": size})
    hls.append({"type": "hl", "extra": "motor_stepper_motor_nema_17_jack","width": 3, "height": 3, "thickness": 12, "size": size})
    hls.append({"type": "hl", "extra": "motor_stepper_motor_nema_17_both","width": 4, "height": 3, "thickness": 12, "size": size})


    #electronics
        #microswitch_standard
    hls.append({"type": "hl", "extra": "electronics_microswitch_standard","width": 3, "height": 3, "thickness": 3, "size": size}) 
    hls.append({"type": "hl", "extra": "electronics_microswitch_standard","width": 3, "height": 3, "thickness": 6, "size": size})            
        #potentimeter_17
    hls.append({"type": "hl", "extra": "electronics_potentiometer_17","width": 3, "height": 3, "thickness": 3, "size": size})
    hls.append({"type": "hl", "extra": "electronics_potentiometer_17","width": 3, "height": 3, "thickness": 12, "size": size})
    hls.append({"type": "hl", "extra": "electronics_potentiometer_17","width": 3, "height": 4, "thickness": 12, "size": size})
        #pushbutton_11
    hls.append({"type": "hl", "extra": "electronics_pushbutton_11","width": 3, "height": 3, "thickness": 3, "size": size})
    hls.append({"type": "hl", "extra": "electronics_pushbutton_11","width": 3, "height": 3, "thickness": 21, "size": size})
    hls.append({"type": "hl", "extra": "electronics_pushbutton_11","width": 3, "height": 4, "thickness": 21, "size": size})
    hls.append({"type": "hl", "extra": "electronics_pushbutton_11_x4","width": 3, "height": 3, "thickness": 3, "size": size})
    hls.append({"type": "hl", "extra": "electronics_pushbutton_11_x4","width": 3, "height": 3, "thickness": 21, "size": size})
    hls.append({"type": "hl", "extra": "electronics_pushbutton_11_x4","width": 3, "height": 4, "thickness": 21, "size": size})
        #mcu
    hls.append({"type": "hl", "extra": "electronics_mcu_atmega328_shennie","width": 3, "height": 4, "thickness": 6, "size": size})


    return hls


def get_jas(size="oobb"):
    jas = []

    types = ["ja", "jab"]

    for typ in types:
        for wid in range(3, 10+1):
            jas.append({"type": typ, "width": wid, "height": 1,
                    "thickness": 12, "size": size})

    jas.append({"type": "ja", "width": 3, "height": 2,
               "thickness": 12, "size": size})
    jas.append({"type": "ja", "width": 5, "height": 2,
               "thickness": 12, "size": size})
    jas.append({"type": "ja", "width": 3, "height": 3,
               "thickness": 12, "size": size})

    jas.append({"type": "jab", "width": 2, "height": 1,
               "thickness": 12, "size": size})
    jas.append({"type": "jab", "width": 1, "height": 1,
               "thickness": 12, "size": size})

    return jas

def get_jgs(size="oobb"):
    jgs = []

    jgs.append({"type": "jg", "extra": "tr_03_03","width": 5, "height": 5, "thickness": 6, "size": size})    
    jgs.append({"type": "jg", "extra": "screw_sorter_m3_03_03","width": 3, "height": 3, "thickness": 15, "size": size})
            


    return jgs


def get_mps(size="oobb"):
    mounting_plates = []
    # bigtree octopur driver board
    mounting_plates.append({"type": "mp", "width": 13, "height": 9, "thickness": 3, "width_mounting": 150,
                           "height_mounting": 90, "radius_hole": "m3", "name": "bigtreetech_octopus", "size": size})

    # e3d titan extruder
    mounting_plates.append({"type": "mpu", "width": 6, "height": 3, "thickness": 3, "width_mounting": 54,
                           "height_mounting": 15, "radius_hole": "m4", "name": "e3d_extruder_titan", "size": size})
    mounting_plates.append({"type": "mps", "width": 5, "height": 3, "thickness": 3, "width_mounting": 54,
                           "height_mounting": 15, "radius_hole": "m4", "name": "e3d_extruder_titan", "size": size})
    mounting_plates.append({"type": "mpt", "width": 6, "height": 2, "thickness": 3, "width_mounting": 54,
                           "height_mounting": 15, "radius_hole": "m4", "name": "e3d_extruder_titan", "size": size})

    # aliexpress motor controller
    mounting_plates.append({"type": "mp", "width": 4, "height": 4, "thickness": 3, "width_mounting": 26,
                           "height_mounting": 26, "radius_hole": "m3", "name": "aliexpress_motor_controller_speed", "size": size})
    mounting_plates.append({"type": "mpu", "width": 3, "height": 3, "thickness": 3, "width_mounting": 26,
                           "height_mounting": 26, "radius_hole": "m3", "name": "aliexpress_motor_controller_speed", "size": size})
    mounting_plates.append({"type": "mps", "width": 3, "height": 3, "thickness": 3, "width_mounting": 26,
                           "height_mounting": 26, "radius_hole": "m3", "name": "aliexpress_motor_controller_speed", "size": size})

    return mounting_plates


def get_pls(size="oobb"):
    plates = []
    
    
    sizes = ["oobb", "oobe"]
    
    for size in sizes:
        #all 3m thicks 1x1 to 10x10
        for wid in range(1, 10):
            for hei in range(1, 10):
                if wid >= hei:
                    plates.append({"type": "pl", "width": wid,
                                "height": hei, "thickness": 3, "size": size})

        #all thicknesses 1x1
        depths = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        for dep in depths:
            plates.append({"type": "pl", "width": 1, "height": 1,
                    "thickness": dep, "size": size})
        
        #various plates that also have extra thicknesses
        premo_plates = []
        premo_plates.append([2,1])
        premo_plates.append([3,1])
        premo_plates.append([4,1])
        premo_plates.append([5,1])
        premo_plates.append([7,1])
        premo_plates.append([9,1])
        premo_plates.append([10,1])
        premo_plates.append([11,1])
        premo_plates.append([12,1])
        premo_plates.append([13,1])
        premo_plates.append([15,1])
        premo_plates.append([17,1])
        premo_plates.append([19,1])
        premo_plates.append([20,1])
        premo_plates.append([2,1])
        premo_plates.append([3,3])
        premo_plates.append([5,5])
        premo_thicknesses = [6, 9, 12, 15,21,30]
        for plate in premo_plates:
            for thickness in premo_thicknesses:
                plates.append({"type": "pl", "width": plate[0], "height": plate[1],
                    "thickness": thickness, "size": size})

        #one widers
        for len in range(2, 35):
            plates.append({"type": "pl", "width": len, "height": 1,
                        "thickness": 3, "size": size})

        #03s, 05s
        widths = [7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        heights = [3,5]
        for w in widths:
            for h in heights:
                plates.append({"type": "pl", "width": w, "height": h,
                        "thickness": 3, "size": size})
        
        #squares
        widths = range(10,21)
        for w in widths:
            plates.append({"type": "pl", "width": w, "height": w,
                    "thickness": 3, "size": size})
        
        # larger plates of desire
        plates.append({"type": "pl", "width": 15, "height": 9,
                    "thickness": 3, "size": size})

        
        # extra fifteens
        widths = range(1,21)        
        for w in widths:
                if w < 15:
                    plates.append({"type": "pl", "width": 15, "height": w,
                        "thickness": 3, "size": size})
                else:
                    plates.append({"type": "pl", "width": w, "height": 15,
                        "thickness": 3, "size": size})
        
        plates.append({"type": "pl", "width": 15, "height": 14,
                    "thickness": 3, "size": size})
        plates.append({"type": "pl", "width": 15, "height": 13,
                    "thickness": 3, "size": size})
        plates.append({"type": "pl", "width": 15, "height": 12,
                    "thickness": 3, "size": size})
        plates.append({"type": "pl", "width": 15, "height": 11,
                    "thickness": 3, "size": size})

    size = "oobb"
    plates.append({"type": "pl", "width": 28, "height": 20,
                "thickness": 3, "size": size, "name": "oobb_pl_a3"})
    plates.append({"type": "pl", "width": 20, "height": 14,
                "thickness": 3, "size": size, "name": "oobb_pl_a4"})
    plates.append({"type": "pl", "width": 14, "height": 10,
                "thickness": 3, "size": size, "name": "oobb_pl_a5"})
    plates.append({"type": "pl", "width": 10, "height": 7,
                "thickness": 3, "size": size, "name": "oobb_pl_a6"})


    size = "oobe"
    thicknesses = [3]
    for thickness in thicknesses:
        plates.append({"type": "pl", "width": 28, "height": 20, "thickness": thickness, "size": size, "name": "oobe_warehouse_box"})
        plates.append({"type": "pl", "width": 21, "height": 21, "thickness": thickness, "size": size, "name": "oobe_shelf_tray"})
    

    #add oobe holes to all oobb plates
    for plate in plates:
        #add "both_holes" True to all plates
        if plate["size"] == "oobb":
            plate["both_holes"] = True

    

    size = "oobb"

    #non both_holes ones
    #gorm plates
    plates.append({"type": "pl", "width": 7, "height": 4,
                  "thickness": 3, "extra":"gorm", "size": size})
    plates.append({"type": "pl", "width": 5, "height": 2,
                  "thickness": 3, "extra":"gorm", "size": size})


    return plates


def get_shs(size="oobb"):
    shafts = []
    thinesses = [0, 0.5, 1, 3, 3.5, 4, 6, 9, 12, 15]
    extras = ["","small", "countersunk", "countersunk_small", "nut", "nut_small"]
    for extra in extras:
        for dep in thinesses:
            shafts.append({"type": "sh", "thickness": dep, "size": size, "extra": extra})
    

    return shafts


def get_scs(size="oobb"):
    couplers = []
    size = "oobb"
    couplers.append({"type": "sc", "diameter": 2, "thickness": 9,  "size": size})
    
    return couplers

def get_sjs(size="oobb"):
    sjs = []
    
    sjs.append({"type": "sj", "extra": "electronics_mcu_pi_pico_socket", "width": 3, "height": 5, "thickness": 9, "size": size})
    



    return sjs


def get_ths(size="oobb"):
    tool_holders = []
    size = "oobb"
    tool_holders.append({"type": "th", "width": 7, "height": 10,  "thickness": 66, "extra": "tool_holder_basic", "size": size})


    #C:\DB\Dropbox\bbbb_product_working\tool\tool_holder

    tools = []

    extra_thick = 2

    tools.append(["tool_pliers_needlenose_generic_130_mm_blue",5,5,10+extra_thick])
    
    ## screwdriver
    tools.append(["tool_screwdriver_hex_wera_60_mm_x4",7,5,18+extra_thick])  
    tools.append(["tool_screwdriver_hex_wera_60_mm_x2",5,5,18+extra_thick])  
    tools.append(["tool_screwdriver_hex_m1d5_wera_60_mm",3,5,18+extra_thick])  
    tools.append(["tool_screwdriver_hex_m2_wera_60_mm",3,5,18+extra_thick])  
    tools.append(["tool_screwdriver_hex_m2d5_wera_60_mm",3,5,18+extra_thick])
    tools.append(["tool_screwdriver_multi_quikpik_200_mm_knife",5,5,36+extra_thick]) 
    tools.append(["tool_screwdriver_driver_bit",3,3,8+extra_thick])
    tools.append(["tool_screwdriver_driver_bit_x4",5,3,8+extra_thick])
    tools.append(["tool_screwdriver_driver_bit_x6",7,3,8+extra_thick])
    tools.append(["tool_screwdriver_driver_bit_x8",9,3,8+extra_thick])
    tools.append(["tool_screwdriver_hex_key_set_small",5,5,6+extra_thick])
    tools.append(["tool_screwdriver_hex_key_set_small_reverse",5,5,6+extra_thick])

    tools.append(["tool_marker_sharpie",3,5,13+extra_thick])
    tools.append(["tool_marker_sharpie_x2",5,5,13+extra_thick])

    #tools.append(["tool_knife_exacto_17mm_black",3,5,12]) # too thick
    tools.append(["tool_side_cutters_generic_110_mm_red",5,5,11+extra_thick])
    tools.append(["tool_wire_strippers_generic_120_red",5,5,11+extra_thick])
    tools.append(["tool_wrench_m7",3,5,4.5+extra_thick])
    tools.append(["tool_wrench_m8",3,5,5.5+extra_thick])
    tools.append(["tool_wrench_m10",3,5,7+extra_thick])
    tools.append(["tool_wrench_m10_x2",5,5,7+extra_thick])
    tools.append(["tool_wrench_m10_x3",7,5,7+extra_thick])
    tools.append(["tool_wrench_m10_x4",9,5,7+extra_thick])
    tools.append(["tool_wrench_m13",3,5,8+extra_thick])
    tools.append(["tool_wrench_m21",5,5,10+extra_thick])
    
    tools.append(["tool_knife_exacto_17mm_black",3,5,27.5+extra_thick])

    #tdpb tools
    tools.append(["tool_tdpb_nozzle_changer",3,5,12+extra_thick])
    tools.append(["tool_tdpb_drill_cleaner_m3",3,5,15+extra_thick])
    tools.append(["tool_tdpb_drill_cleaner_m6",3,5,15+extra_thick])
    tools.append(["tool_tdpb_glue_stick_prit_medium_knife",5,5,28+extra_thick])
    tools.append(["tool_tdpb_glue_stick_prit_medium",4,5,28+extra_thick])

    #specialty tools
    tools.append(["tool_electronics_crimp_jst_wc_260",5,5,24+extra_thick])

    for tool in tools:
        tool_holders.append({"type": "thv", "width": tool[1], "height": tool[2],  "thickness": tool[3], "extra": tool[0], "size": size})
    return tool_holders

def get_trs(size="oobb"):
    trays = []

    ts = []    
    """
    ts.append([3,1])    
    ts.append([2,1])
    ts.append([3,1.5])    
    ts.append([2,2])    
    ts.append([3,2])
    ts.append([4,2])
    ts.append([5,2])
    ts.append([2,2.5])
    ts.append([3,2.5])
    ts.append([4,2.5])
    ts.append([5,3])
    ts.append([4,3])
    ts.append([3,3])
    ts.append([4,4])
    ts.append([5,5])
    """
    ts.append([3,3])

    thicknesses = [12, 15, 18, 21, 24, 27, 30]
    for tray in ts:
        trays.append({"type": "trl", "width": tray[0], "height": tray[1], "thickness": 2, "size": size})
        trays.append({"type": "trlt", "width": tray[0], "height": tray[1], "thickness": 4, "size": size})
        trays.append({"type": "trlts", "width": tray[0], "height": tray[1], "thickness": 4, "size": size})
        for thickness in thicknesses:
            trays.append({"type": "tr", "width": tray[0], "height": tray[1], "thickness": thickness, "size": size})
            #trv vertical ones with oobb added for mounting on a wall
            trays.append({"type": "trv", "width": tray[1], "height": tray[0], "thickness": thickness, "size": size})
            #trt thin trays for faster printing
            trays.append({"type": "trt", "width": tray[1], "height": tray[0], "thickness": thickness, "size": size})
            #trts thin trays for faster printing with a screw holder
            trays.append({"type": "trts", "width": tray[1], "height": tray[0], "thickness": thickness, "size": size})


    return trays

def get_whs(size="oobb"):
    wheels = []
    types = [["wh",6],["bw",9],["bw",15]]
    for t in types:
        type, thickness = t
        wheels.append({"type": type, "thickness": thickness, "oring_type":"314", "size": size})        
        wheels.append({"type": type, "thickness": thickness, "oring_type":"319", "size": size})
        wheels.append({"type": type, "thickness": thickness, "oring_type":"323", "size": size})
        wheels.append({"type": type, "thickness": thickness, "oring_type":"327", "size": size})
        wheels.append({"type": type, "thickness": thickness, "oring_type":"333", "size": size})
        wheels.append({"type": type, "thickness": thickness, "oring_type":"339", "size": size})

    #make both_holes true for all
    for wheel in wheels:
        wheel["both_holes"] = True


    return wheels


def get_wis(size="oobb"):
    wis = []
    thicknesses = [3,6]
    widths = [2,3]
    extras = ["m2","ba","hv","i2"]
    for thickness in thicknesses:        
        for width in widths:
            for extra in extras:
                wis.append({"type": "wi", "extra": extra, "thickness": thickness, "width": width, "height": 3, "size": size})
    for extra in extras:
        wis.append({"type": "wi", "extra": f'{extra}_base', "thickness": 6, "width": 3, "height": 3, "size": size})  
    
    #base plates
    wis.append({"type": "wi", "extra": "base", "thickness": 3, "width": 2, "height": 3, "size": size})                    
    wis.append({"type": "wi", "extra": "base", "thickness": 3, "width": 
    3, "height": 3, "size": size})                    
    wis.append({"type": "wi", "extra": "base_cap", "thickness": 3, "width": 3, "height": 3, "size": size})                    
    #wis.append({"type": "wi", "extra": "base_holder", "thickness": 3, "width": 3, "height": 3, "size": size})                    
    
    #cap    
    wis.append({"type": "wi", "extra": "cap", "thickness": 3, "width": 3, "height": 3, "size": size})                    
    
    
    
    #spacer    
    thicknesses = [3,6,9,12]
    for thickness in thicknesses:
        wis.append({"type": "wi", "extra": "spacer", "thickness": thickness, "width": 3, "height": 3, "size": size})  
        wis.append({"type": "wi", "extra": "spacer_long", "thickness": thickness, "width": 3, "height": 3, "size": size}) 
        wis.append({"type": "wi", "extra": "spacer_u", "thickness": thickness, "width": 3, "height": 3, "size": size})                    
    

    return wis

def get_zts(size="oobb"):

    zts = []

    zts.append({"type": "ztj", "width": 1, "thickness": 12, "size": size})
    zts.append({"type": "ztj", "width": 1, "height": 2,
               "thickness": 12, "size": size})
    zts.append({"type": "ztj", "width": 2, "thickness": 12, "size": size})
    zts.append({"type": "ztj", "width": 2, "height": 2,
               "thickness": 12, "size": size})
    zts.append({"type": "ztj", "width": 2, "height": 3,
               "thickness": 12, "size": size})
    zts.append({"type": "ztj", "width": 3, "thickness": 12, "size": size})

    zts.append({"type": "zt", "width": 2, "height": 3,
               "thickness": 6, "size": size})
    zts.append({"type": "zt", "width": 2, "height": 4,
               "thickness": 6, "size": size})
    zts.append({"type": "zt", "width": 2, "height": 5,
               "thickness": 6, "size": size})

    return zts

# other makes


def get_bearings():
    bearings = []
    bearing_names = ['6701', '6702', '6703', '6704', '6705', '6706', '6707', '6800', '6801', '6802', '6803', '6804', '6805', '6806', '6807', '6808',
                     '6809', '6810', '6811', '6812', '6813', '6814', '6815', '6816', '6817', '6818', '6819', '6820', '6821', '6822', '6824', '6826', '6828', '6830']

    for bearing in bearing_names:
        bearings.append(
            {"type": "bearing", "bearing_name": bearing, "size": "hardware"})

    return bearings


def get_nuts():
    nuts = []
    nut_sizes = ["m1d5", "m2", "m3", "m4", "m5", "m6", "m8", "m10", "m12"]
    # nut_sizes = ["m10", "m12"]
    for nut_size in nut_sizes:
        nuts.append(
            {"type": "nut", "radius_name": nut_size, "size": "hardware"})

    standoff_lengths = [6, 8, 10, 12, 15, 20, 25, 30]
    standoff_radiuses = ["m3"]
    for standoff_radius in standoff_radiuses:
        for standoff_length in standoff_lengths:
            nuts.append({"type": "standoff", "radius_name": standoff_radius,
                        "depth": standoff_length, "size": "hardware"})

    threaded_insert_radiuses = ["m3"]
    for threaded_insert_radius in threaded_insert_radiuses:
        nuts.append({"type": "threaded_insert",
                    "radius_name": threaded_insert_radius, "size": "hardware"})

    return nuts


def get_screws():
    screws = []
    sizes = {}
    sizes["m3"] = [8, 10, 12, 16, 18, 20, 25, 30, 35, 40]
    for size in sizes:
        for depth in sizes[size]:
            screws.append({"type": "screw_countersunk",
                          "radius_name": size, "depth": depth, "size": "hardware"})
            screws.append({"type": "screw_socket_cap",
                          "radius_name": size, "depth": depth, "size": "hardware"})

    sizes = {}
    lengths = [6, 12, 16, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    sizes["m5"] = lengths
    sizes["m6"] = lengths
    for size in sizes:
        for depth in sizes[size]:
            screws.append({"type": "bolt", "radius_name": size,
                          "depth": depth, "size": "hardware"})

    return screws


def get_tests():
    tests = []

    #hole test
    tests.append({"type": "test", "size": "test", "shape": "oobb_hole",
                 "name_variable": "hole_radius", "radius_name": "m5", "depth": 4, "depth2":3, "difference": 0.1})


    # nut test
    tests.append({"type": "test", "size": "test", "shape": "oobb_nut",
                 "name_variable": "nut_radius", "radius_name": "m3", "depth": 4, "difference": 0.1, "z": -3})

    style = "01"
    tests.append({"type": "test", "size": "test", "shape": "oobb_threaded_insert", "name_variable": f"threaded_insert_{style}_radius", "style": style, "radius_name": "m3", "depth": 7, "difference": 0.1, "hole": False})
    tests.append({"type": "test", "size": "test", "shape": "oobb_threaded_insert", "name_variable": f"threaded_insert_{style}_insertion_cone", "style": style, "radius_name": "m3", "depth": 4, "difference": 0.1, "hole": False, "depth_adjust":3, "insertion_cone":True, "name":"insertion_cone", "padding":9})
    
    return tests

    for thing in things:
        oobb_base.add_thing(thing)

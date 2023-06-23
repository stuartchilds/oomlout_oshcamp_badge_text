import opsc
import oobb
import oobb_base as ob
import oobb_get_items_oobb as obo
import opsc_library_gen
import os

#name_project equals module name
name_project = __file__.split('\\')[-1].split('.')[0]

save_type="all"
#save_type="none"


def all():
    obs = {}
    objects = []    
    
    ##oobb_cube_center
    width = 10
    height = 10
    depth = 10        
    x,y,z = 0,0,0
    shap = "oobb_cube_center"
    objects.append(ob.oe(t="p", s=shap, size=[width,height,depth], pos=[x,y,z], m=""))
    ##oobb_cube_center
    ins = "cube"
    oin = obs[ins] = {}
    oin["width"] = 10
    oin["height"] = 10
    oin["depth"] = 10
    oin["x"], oin["y"], oin["z"] = 0,0,0
    oin["shap"] = "oobb_cube_center"
    objects.append(ob.oe(t="p", s=oin["shap"], size=[oin["width"],oin["height"],oin["depth"]], pos=[oin["x"],oin["y"],oin["z"]], m=""))
    



    ##oobb_cylinder
    radius = 10    
    depth = 10
    x,y,z = 0,0,0
    shap = "oobb_cylinder"
    objects.append(ob.oe(t="p", s=shap, radius=radius, depth=depth, pos=[x,y,z], m=""))

    ##oobb_hole
    radius_name = "m3"
    depth = 10
    x,y,z = 0,0,0
    shap = "oobb_hole"
    objects.append(ob.oe(t="n", s=shap, radius_name=radius_name, depth=depth, pos=[x,y,z], m=""))

    ##oobb_countersunk
    rotY = 0 #change to 180 to flip
    radius_name = "m3"
    depth = 10
    x,y,z = 0,0,0
    shap = "oobb_countersunk"
    objects.append(ob.oe(t="n", s=shap, radius_name=radius_name, include_nut=False, depth=depth, rotY=rotY,pos=[x,y,z], m=""))

    ##oobb_rounded_rectangle
    width = 10
    height = 10
    depth = 10
    x,y,z = 0,0,0
    shap = "rounded_rectangle"
    objects.append(ob.oe(t="p", s=shap, size=[width,height,depth], pos=[x,y,z], m=""))


    #oobb pl
    width = 3
    height = 3
    depth = 3
    x,y,z = 0,0,0
    shap = "oobb_pl"    
    objects.append(ob.oe(t="p", s=shap, width=width, height=height, depth=depth, pos=[x,y,z], holes=False, m="#"))
    
    ###### oobb item
    details = {"type": "wi", 
               "extra": "base", 
               "thickness": 3, 
               "width": 3, 
               "height": 3, 
               "size": "oobb"} ##from make_sets
    objects.append(obo.get_wi(**details)["components"])
    
    ## oobb_plate
    x=112.5
    y=0
    z=0
    details = {"type": "pl", "width": 1, "height": 3,"thickness": 3, "size": "oobb", "both_holes":True, "pos":[x,y,z]}
    objects.append(obo.get_pl(**details)["components"])
    x=112.5#

    #slice
    x,y,z = 0,0,0
    objects.append(ob.oe(t="n", s="oobb_slice", pos=[x,y,z], m="")) 

    return objects
    

def main():
    
    make_badge()

    #read lines from data.txt into an array
    with open("data.txt") as f:
        lines = f.readlines()
        #remove whitespace characters like `\n` at the end of each line
        lines = [x.strip() for x in lines]
        for line in lines:
            obs = {}
            objects = []    
    
            name = line      

            #if name is 5 charachters or less
            if len(name) <= 5:
                ##text
                ins = "text1"
                oin = obs[ins] = {}
                #first is equal to the first five letters of line in upper case
                first = name[:5].upper()
                oin["text"] = first
                oin["size"] = 13
                oin["height"] = 8
                oin["font"] = "DejaVu Sans Mono:style=Bold" # "Liberation Sans:style=Bold Italic"
                oin["halign"] = "center"
                oin["valign"] = "center"
                oin["wall_thickness"] = 0.5
                oin["x"], oin["y"], oin["z"] = 0,0,0
                oin["shap"] = "text_hollow" #text_hollow text
                objects.append(ob.oe(t="p", s=oin["shap"], text=oin["text"], size=oin["size"], font=oin["font"], halign=oin["halign"], valign=oin["valign"], height=oin["height"], pos=[oin["x"],oin["y"],oin["z"]], m="", extra="reverse"))
            else:
                #add a "-" as the 5th character
                name1 = name[:4] + "-" + name[4:]
                first = name1[:5].upper()
                second = name1[5:10].upper()
                ins = "text2"
                oin = obs[ins] = {}
                #first is equal to the first five letters of line in upper case
                oin["text"] = first
                oin["size"] = 13
                oin["height"] = 8
                oin["font"] = "DejaVu Sans Mono:style=Bold" # "Liberation Sans:style=Bold Italic"
                oin["halign"] = "center"
                oin["valign"] = "center"
                oin["wall_thickness"] = 0.5
                oin["x"], oin["y"], oin["z"] = 0,10.5,0
                oin["shap"] = "text_hollow" #text_hollow text
                objects.append(ob.oe(t="p", s=oin["shap"], text=oin["text"], size=oin["size"], font=oin["font"], halign=oin["halign"], valign=oin["valign"], height=oin["height"], pos=[oin["x"],oin["y"],oin["z"]], m="", extra="reverse"))

                oin["text"] = second
                oin["x"], oin["y"], oin["z"] = 0,-10.5,0
                objects.append(ob.oe(t="p", s=oin["shap"], text=oin["text"], size=oin["size"], font=oin["font"], halign=oin["halign"], valign=oin["valign"], height=oin["height"], pos=[oin["x"],oin["y"],oin["z"]], m="", extra="reverse"))

            #oobb pl
            width = 5
            height = 3
            depth = 0.5
            x,y,z = 0,0,0
            shap = "oobb_pl"    
            objects.append(ob.oe(t="p", s=shap, width=width, height=height, depth=depth, pos=[x,y,z], holes=False, m=""))
            
            hs = []
            hs.append([1,1])
            hs.append([1,2])
            hs.append([1,3])
            hs.append([5,1])
            hs.append([5,2])
            hs.append([5,3])
            
            ##oobb_hole
            radius_name = "m3"
            x,y,z = 0,0,0
            pos = [x,y,z]
            width = width
            height = height
            holes  = ["single"] # "single"
            loc = hs
            shap = "oobb_holes"
            objects.append(ob.oe(t="n", s=shap, radius_name=radius_name, pos=pos, width=width, height=height, loc=hs,holes = holes, m=""))



            #output filename test
            filename = f"outputs/{name}/3dpr.scad"
            #make directory for filename
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            #if filename doesn't exist

            if not os.path.exists(filename):
                ob.build_thing_filename(filename=f'outputs/{name}/', thing=objects, save_type=save_type, render=True)
            else:
                #print meassage about skipping because file already exists
                print(f"skipping {filename} because it already exists")
            #copy the outputs/name/3dpr.stl to a outputs/stl directory overwrite if it already exists using os
            import shutil
            #if directory doesn't exist make it
            os.makedirs(os.path.dirname(f"outputs/stl/{name}.stl"), exist_ok=True)
            shutil.copyfile(f"outputs/{name}/3dpr.stl", f"outputs/stl/{name}.stl")
            #copy the outputs/name/3dpr.scad to a outputs/scad directory overwrite if it already exists
            os.makedirs(os.path.dirname(f"outputs/scad/{name}.scad"), exist_ok=True)
            shutil.copyfile(f"outputs/{name}/3dpr.scad", f"outputs/scad/{name}.scad")
        

X = 0
Y = 1
Z = 2


def make_badge():
    obs = {}
    objects = []    
    
    #oobb pl
    width = 5
    height = 8
    depth = 1.6
    x,y,z = 0,0,0
    shap = "oobb_pl"    
    objects.append(ob.oe(t="p", s=shap, width=width, height=height, depth=depth, pos=[x,y,z], holes=False, m=""))
    
    hs = []
    hs.append([1,1])
    hs.append([1,3])
    hs.append([1,4])
    hs.append([1,5])
    hs.append([1,6])
    hs.append([1,7])
    hs.append([1,8])
    hs.append([2,1])
    hs.append([3,1])
    hs.append([5,1])
    hs.append([5,2])
    hs.append([5,3])
    hs.append([5,4])
    hs.append([5,5])
    hs.append([5,6])
    hs.append([5,7])
    hs.append([5,8])
    
    ##oobb_hole
    radius_name = "m3"
    x,y,z = 0,0,0
    pos = [x,y,z]
    width = width
    height = height
    holes  = ["single"] # "single"
    loc = hs
    shap = "oobb_holes"
    objects.append(ob.oe(t="n", s=shap, radius_name=radius_name, pos=pos, width=width, height=height, loc=loc,holes = holes, m=""))



    #only make if stl doesn't exist
    filename = f"outputs/0_badge/3dpr.stl"
    #make directory for filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    #if filename doesn't exist
    if not os.path.exists(filename):
        ob.build_thing_filename(filename=f'outputs/0_badge/', thing=objects, save_type=save_type)

if __name__ == "__main__":
    main()
    

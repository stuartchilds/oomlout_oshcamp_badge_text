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
    obs = {}
    objects = []    
    

    #read lines from data.txt into an array
    with open("data.txt") as f:
        lines = f.readlines()
        #remove whitespace characters like `\n` at the end of each line
        lines = [x.strip() for x in lines]
        for line in lines:
            name = line      

            ##text
            ins = "text1"
            oin = obs[ins] = {}
            oin["text"] = line
            oin["size"] = 17
            oin["height"] = 8
            oin["font"] = "DejaVu Sans Mono:style=Bold" # "Liberation Sans:style=Bold Italic"
            oin["halign"] = "center"
            oin["valign"] = "center"
            oin["wall_thickness"] = 0.5
            oin["x"], oin["y"], oin["z"] = 0,0,0
            oin["shap"] = "text_hollow" #text_hollow text
            objects.append(ob.oe(t="p", s=oin["shap"], text=oin["text"], size=oin["size"], font=oin["font"], halign=oin["halign"], valign=oin["valign"], height=oin["height"], pos=[oin["x"],oin["y"],oin["z"]], m="", extra="reverse"))


            #joining piece
            width = (7.5*10)-1
            height = 7.5*3-1
            depth = 0.5
            x,y,z = 0,0,0
            shap = "rounded_rectangle"
            radius = 1
            objects.append(ob.oe(t="p", s=shap, r=radius, size=[width,height,depth], pos=[x,y,z], m=""))
            
            xs = [7.5 * 9/2,-7.5 * 9/2]
            ys = [7.5, 0, -7.5]
            for x in xs:
                for y in ys:
                    objects.append(ob.oe(t="n", s="oobb_hole", radius_name="m3", depth=100, pos=[x,y,-50], m="#"))


            #output filename test
            filename = f"outputs/{name}/3dpr.scad"
            #if filename doesn't exist
            if not os.path.exists(os.path.dirname(filename)):
                ob.build_thing_filename(filename=f'outputs/{name}/', thing=objects, save_type=save_type, render=False)

X = 0
Y = 1
Z = 2


if __name__ == "__main__":
    main()
    

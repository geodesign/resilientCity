# --------------------------------
# Name: Create_Asset_Range.py
# Purpose: Walk a directory and print a @range annotation for CGA rules.
# Current Owner: David Wasserman
# Last Modified: 09/08/2017
# Copyright:   (c) CoAdapt
# ArcGIS Version:   10.4.1
# Python Version:   3.5
# --------------------------------
# Copyright 2016 David J. Wasserman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------
import glob,os


def asset_directory_utility(list_of_dir_paths):
    path_dict={}
    for path in list_of_dir_paths:
        print("Gathering files from path: {0}".format(path))
        file_names=[]
        range_string='@Range('
        string_list=''
        file_list=glob.glob(path+r"\*.jpg")
        for file in file_list:
            file_name=os.path.split(file)[1]
            file_names.append(file_name)
            file_name_no_ext= os.path.splitext(file_name)[0]
            range_string=range_string+'"'+file_name_no_ext+'"'+','
            string_list= string_list+file_name_no_ext+';'
        range_string=range_string.strip(",")+")"
        path_dict[path]={"files":file_names,"range":range_string,"string_list":string_list}

    return path_dict

if __name__=="__main__":
    root_asset=r"D:\Documents\CityEngine\CEProjects\slr-master\SLR_Adaptation_Project\assets\SLRLotTextures"
    paths = [root_asset+r"\WallTextures",root_asset+r"\Vegetation\Grass",root_asset+r"\Frames",
             root_asset + r"\SlopedRoof",root_asset+r"\FlatRoof"]
    asset_dict=asset_directory_utility(paths)
    for path in asset_dict:
        file_names=asset_dict[path]["files"]
        range_string = asset_dict[path]["range"]
        string_list = asset_dict[path]["string_list"]
        #print(file_names)
        print(path)
        print(range_string)
        print(string_list)

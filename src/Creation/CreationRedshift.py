import c4d

from ..Const import Const
from CreationFunction import CreationFunction

const = Const()

class CreationRedshift(CreationFunction):
    def refresh_redshift_light(self, dialog, list_lights):
        save_light = dialog.GetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT)

        #Name
        self.create_edit_string(dialog, const.LIGHT_LISTER_REDSHIFT_NAME,
                                "Name", const.OBJ, list_lights, True)

        try:
            current_light = dialog.GetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT)
            decalage = save_light["x2"] - current_light["x2"]
            size_x = current_light["x2"] - current_light["x1"]
            if decalage > 0 and current_light["x1"] < size_x :
                decalage = 0 - decalage
            dialog.SetVisibleArea(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT,
                                  current_light["x1"] + decalage,
                                  current_light["y1"],
                                  current_light["x2"] + decalage,
                                  current_light["y2"]
                                  )
        except:
            pass


    def create_redshift_light(self, dialog, config, list_lights, layers):
        if not len(list_lights):
            return

        dialog.ScrollGroupBegin(const.GRP_TAB_REDSHIFT_SCROLL_NAME, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_LEFT | c4d.SCROLLGROUP_AUTOVERT, 0, 0)
        if dialog.GroupBegin(const.GRP_TAB_REDSHIFT_GRP, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, 300, 200, "Redshift"):
            dialog.GroupBorderSpace(0, 0, 10, 15)

            self.create_min_max_button(dialog, const.LIGHT_LISTER_REDSHIFT_ORDER_GRP, const.LIGHT_LISTER_REDSHIFT_ORDER_UP, const.LIGHT_LISTER_REDSHIFT_ORDER_DOWN, list_lights)

            #select
            self.create_button(dialog, const.LIGHT_LISTER_REDSHIFT_SELECT,
                             "Select", "S", list_lights)

            #Name
            self.create_edit_string(dialog, const.LIGHT_LISTER_REDSHIFT_NAME,
                                  "Name", const.OBJ, list_lights)

            self.create_enable(dialog, const.LIGHT_LISTER_REDSHIFT_ENABLE, list_lights)

        dialog.GroupEnd()
        dialog.GroupEnd()

        dialog.ScrollGroupBegin(const.GRP_TAB_REDSHIFT_SCROLL_LIGHT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_HORIZ | c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_AUTOVERT , 0, 0)
        if dialog.GroupBegin(const.GRP_TAB_REDSHIFT_GRP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 300, 200, "Redshift"):
            if config["visibilityviewport"]:
                buffer = [{"id": 2, "text": "Default"},
                          {"id": 0, "text": "On"},
                          {"id": 1, "text": "Off"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_ENABLE_VIEWPORT,
                                       "Viewport", buffer, const.OBJ, list_lights, c4d.ID_BASEOBJECT_VISIBILITY_EDITOR)

            if config["Visibilityrender"]:
                buffer = [{"id": 2, "text": "Default"},
                          {"id": 0, "text": "On"},
                          {"id": 1, "text": "Off"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_ENABLE_RENDER,
                                       "Render", buffer, const.OBJ, list_lights, c4d.ID_BASEOBJECT_VISIBILITY_RENDER)

            #Light Type
            if config["LightType"]:
                buffer = [{"id": 3, "text": "Area"},
                          {"id": 1, "text": "Point"},
                          {"id": 2, "text": "Spot"},
                          {"id": 0, "text": "Infinite"},
                          {"id": 4, "text": "Dome"},
                          {"id": 5, "text": "IES"},
                          {"id": 6, "text": "Portal"},
                          {"id": 7, "text": "Physical Sun"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_LIGHT_TYPE,
                                       "Light Type", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_TYPE)

            #Preview
            if config["Preview"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_PREVIEW,
                                   "Preview", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PREVIEW)

            #Show Illum
            if config["ShowIllum"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_SHOW_ILLUM,
                                   "Show Illum", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_SHOW_ILLUMINATION)

            #Affects Diffuse
            if config["AffectsDiffuse"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_AFFECT_DIFFUSE,
                                   "Affects Diffuse", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_AFFECTS_DIFFUSE)

            #Affects Specular
            if config["AffectsSpecular"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_AFFECT_SPECULAR,
                                   "Affects Specular", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_AFFECTS_SPECULAR)

            #Color mode
            if config["Colormode"]:
                buffer = [{"id": 0, "text": "Color"},
                          {"id": 1, "text": "Temp"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_COLORMODE,
                                       "Color Mode", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_COLORMODE)

            #Color
            if config["Color"]:
                self.create_color_field(dialog, const.LIGHT_LISTER_REDSHIFT_COLOR,
                                      "Color", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_COLOR)

            #Temp
            if config["Temperature"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_TEMP,
                                      "Temp", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_TEMPERATURE, 1667, 25000)

            #Unit
            if config["Unit"]:
                buffer = [{"id": 0, "text": "Image"},
                          {"id": 1, "text": "Luminous Power"},
                          {"id": 2, "text": "Luminance"},
                          {"id": 3, "text": "Radiant Power"},
                          {"id": 4, "text": "Radiance"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_UNIT,
                                       "Unit", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_UNITSTYPE)

            #Luminous
            if config["Luminous"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_LUMEN,
                                      "Luminous", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_LUMENSPERWATT, -1000.0, 1000.0)

            #Intensity
            if config["LightIntensity"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_INTENSITY,
                                      "Intensity", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_INTENSITY, -2147483648.0, 2147483648.0)

            #Decay Type
            if config["DecayType"]:
                buffer = [{"id": 0, "text": "Inverse Square"},
                          {"id": 1, "text": "None"},
                          {"id": 2, "text": "Linear"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_DECAY_TYPE,
                                       "Decay Type", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_DECAYTYPE)

            #Area Type
            if config["AreaType"]:
                buffer = [{"id": 0, "text": "Rectangle"},
                          {"id": 1, "text": "Disc"},
                          {"id": 2, "text": "Sphere"},
                          {"id": 3, "text": "Cylindre"},
                          {"id": 4, "text": "Mesh"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_GEO,
                                       "Area Type", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_GEOMETRY)

            #SizeX
            if config["AREASizeX"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_SIZEX,
                                      "Size X", const.METER_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SIZEX, 0, 2147483647)

            #SizeY
            if config["AREASizeY"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_SIZEY,
                                      "Size Y", const.METER_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SIZEY, 0, 2147483647)

            #SizeZ
            if config["AREASizeZ"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_SIZEZ,
                                      "Size Z", const.METER_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SIZEZ, 0, 2147483647)

            #Visible in Render
            if config["AREAVisibleinRender"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_VISIBLE_RENDER,
                                      "Visible Render", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_VISIBLE_IN_RENDER)

            #Bidirectional
            if config["AREABidirectional"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_BIDIRECTIONAL,
                                      "Bidirectional", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_BIDIRECTIONAL)

            #Normalize
            if config["AREANormalize"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_NORMALIZE,
                                      "Normalize", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_NORMALIZE)

            #Sample
            if config["AREASample"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_AREA_SAMPLES,
                                      "Sample", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SAMPLES, 0, 1024)

            #Angle
            if config["SPOTAngle"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_SPOT_ANGLE,
                                      "Angle", const.DEGREE_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_SPOT_CONE_ANGLE, 0, 179.9)

            #Faloff angle
            if config["SPOTFaloffangle"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_SPOT_FALLOFF,
                                      "Faloff Angle", const.DEGREE_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_SPOT_CONE_FALLOFF_ANGLE, 0, 179.9)

            #Dome Type
            if config["DomeType"]:
                buffer = [{"id": 0, "text": "Spherical"},
                          {"id": 1, "text": "Hemispherical"},
                          {"id": 2, "text": "Mirror Ball"},
                          {"id": 3, "text": "Angular"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_ENVTYPE,
                                       "Dome Type", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_ENVTYPE)

            #DOMECompensateSRGB
            if config["DOMECompensateSRGB"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_APPLYEXPOSURECOMPENSATION,
                                      "Cam Expo compens", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_APPLYEXPOSURECOMPENSATION)
            #Exposure
            if config["DOMEExposure"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_EXPOSURE,
                                      "Exposure", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_EXPOSURE0, -10, 10)

            #Hue
            if config["DOMEHue"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_HUE,
                                      "Hue", const.DEGREE_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_HUE0, 0, 360)

            #Saturation
            if config["DOMESaturation"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_SATURATION,
                                      "Saturation", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_SATURATION0, 0, 100.0)

            #Tint
            if config["DOMETint"]:
                self.create_color_field(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_TINT,
                                        "Tint", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_COLOR)

            #Sample
            if config["DOMESample"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_DOME_SAMPLE,
                                      "Sample", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_DOME_SAMPLES, 0, 1024)

            #IES Color mode
            if config["IESColormode"]:
                buffer = [{"id": 0, "text": "Color"},
                          {"id": 1, "text": "Temp"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_IES_COLORMODE,
                                       "Color Mode", buffer, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_IES_COLORMODE)

            #IES Color
            if config["IESColor"]:
                self.create_color_field(dialog, const.LIGHT_LISTER_REDSHIFT_IES_COLOR,
                                      "Color", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_IES_COLOR)

            #IES Temp
            if config["IESTemperature"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_IES_TEMP,
                                      "Temp", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_IES_TEMPERATURE, 1667, 25000)

            #IES mult
            if config["IESmult"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_IES_MULT,
                                      "Mult", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_IES_MULTIPLIER, -2147483648, 2147483647)

            #PORTAL sizeX
            if config["PORTALsizeX"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PORTAL_SIZEX,
                                      "Size X", const.METER_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_SIZEX, 0, 2147483647)

            #PORTAL sizeY
            if config["PORTALsizeY"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PORTAL_SIZEY,
                                      "Size Y", const.METER_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_SIZEY, 0, 2147483647)

            #PORTAL mult
            if config["PORTALmult"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PORTAL_MULTIPLIER,
                                      "Mult", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_MULTIPLIER, -100, 100)

            #PORTAL tint
            if config["PORTALtint"]:
                self.create_color_field(dialog, const.REDSHIFT_LIGHT_PORTAL_TINT_COLOR,
                                        "Tint", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_TINT_COLOR)

            #PORTAL Transparency
            if config["PORTALTransparency"]:
                self.create_color_field(dialog, const.REDSHIFT_LIGHT_PORTAL_TRANSPARENCY,
                                        "Transparency", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_TRANSPARENCY)

            #PORTAL samples
            if config["PORTALsamples"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PORTAL_SAMPLES,
                                      "Samples", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_SAMPLES, 0, 1024)

            #SKY Intensity
            if config["SKYIntensity"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_MULTIPLIER,
                                        "Intensity", const.FLOAT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_MULTIPLIER, -2147483648, 2147483648)

            #SKY Non Physical
            if config["SKYNonPhysical"]:
                self.create_checkbox(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY,
                                     "No Physical", const.OBJ, list_lights,
                                     c4d.REDSHIFT_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY)

            #SKY Disk Scale
            if config["SKYDiskScale"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_SUN_DISK_SCALE,
                                        "Disk Scale", const.FLOAT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_SUN_DISK_SCALE, -2147483648, 2147483648)

            #SKY Haze
            if config["SKYHaze"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_HAZE,
                                        "Haze", const.FLOAT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_HAZE, -2147483648, 2147483648)

            #SKY Ozone
            if config["SKYOzone"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_OZONE,
                                        "Ozone", const.FLOAT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_OZONE, 0, 10)

            #SKY Height
            if config["SKYHeight"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_HORIZON_HEIGHT,
                                        "Height", const.FLOAT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_HORIZON_HEIGHT, -2147483648, 2147483648)

            #SKY Red-blue shift
            if config["SKYRed-blueshift"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_REDBLUESHIFT,
                                        "Shift", const.FLOAT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_REDBLUESHIFT, -10, 10)

            #SKY samples
            if config["SKYsaturation"]:
                self.create_number_edit(dialog, const.REDSHIFT_LIGHT_PHYSICALSUN_SATURATION,
                                        "Saturation", const.INT_MODE, const.OBJ, list_lights,
                                        c4d.REDSHIFT_LIGHT_PHYSICALSUN_SATURATION, 0, 1)

            #Vol Contribution
            if config["VolContribution"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_VOLUME,
                                      "Vol Contri", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_VOLUME_RAY_CONTRIBUTION_SCALE, 0, 1)

            #Vol Sample
            if config["VolSample"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_VOLUME_SAMPLE,
                                      "Vol sample", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_VOLUME_NUM_SAMPLES, 0, 1024)

            #Shadow Enable
            if config["EnableShadow"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_SHADOW_ENABLE,
                                     "Shadow", const.OBJ, list_lights,
                                     c4d.REDSHIFT_LIGHT_SHADOW)

            #Shadow Transparecy
            if config["ShadowTransparecy"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_SHADOW_TRANPS,
                                      "Shadow Trans", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_SHADOWTRANSPARENCY, 0, 1)

            #Shadow Contribution
            if config["ShadowSoftness"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS,
                                      "Softness", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_SAMPLINGOVERRIDES_SHADOWSAMPLESSCALE, 0, 100)

            #Shadow Sample
            if config["ShadowSample"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE,
                                      "Shadow sample", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_SAMPLINGOVERRIDES_NUMSHADOWSAMPLES, 0, 1024)

            #Caustics
            if config["Caustics"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_PHOTON_ENABLED,
                                      "Caustics", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_CAUSTICS_ENABLED)

            #Caustics mult
            if config["Causticsmult"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_PHOTON_INTENSITY,
                                      "Caustics mult", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_CAUSTICS_INTENSITY_MULTIPLIER, 0, 100)

            #Caustic num
            if config["Causticnum"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_PHOTON_NUM,
                                      "Caustic num", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_CAUSTICS_NUM_PHOTONS, 0, 2147483647)

            #GI
            if config["GI"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_REDSHIFT_GI_ENABLED,
                                      "GI", const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_GI_ENABLED)

            #GI mult
            if config["GImult"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_GI_MULITPLIER,
                                      "GI mult", const.FLOAT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_GI_INTENSITY_MULTIPLIER, 0, 100)

            #GI num
            if config["GInum"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_REDSHIFT_GI_PHOTONS,
                                      "GI num", const.INT_MODE, const.OBJ, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_GI_NUM_PHOTONS, 0, 2147483647)

            #Layers
            if config["Layers"]:
                buffer = list()
                buffer.append({"id": 0, "text": "None"})
                for i in xrange(len(layers)):
                    buffer.append({"id": i+1, "text": layers[i].GetName()})

                self.create_cycle_button(dialog, const.LIGHT_LISTER_REDSHIFT_LAYERS,
                                       "Layer", buffer, const.OBJ, list_lights, layers=layers)
        dialog.GroupEnd()
        dialog.GroupEnd()

        self.disable_redshift_data(dialog, list_lights, layers)

    def set_area_point_spot_infinite(self, dialog, light_id, state):
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLORMODE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLOR + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_TEMP + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_UNIT + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LUMEN + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_INTENSITY + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DECAY_TYPE + light_id + 2, state)

    def set_area(self, dialog, light_id, state):
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_GEO + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SIZEX + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SIZEY + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SIZEZ + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_VISIBLE_RENDER + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_BIDIRECTIONAL + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_NORMALIZE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SAMPLES + light_id + 2, state)

    def set_spot(self, dialog, light_id, state):
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SPOT_ANGLE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SPOT_FALLOFF + light_id + 2, state)

    def set_dome(self, dialog, light_id, state):
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_PATH + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_ENVTYPE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_OPTIONS_DOME_APPLYEXPOSURECOMPENSATION + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_EXPOSURE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_HUE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_SATURATION + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_TINT + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_SAMPLE + light_id + 2, state)

    def set_ies(self, dialog, light_id, state):
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_PATH + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLORMODE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLOR + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_TEMP + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_MULT + light_id + 2, state)

    def set_portal(self, dialog, light_id, state):
        dialog.Enable(const.REDSHIFT_LIGHT_PORTAL_SIZEX + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PORTAL_SIZEY + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PORTAL_MULTIPLIER + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PORTAL_TINT_COLOR + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PORTAL_TRANSPARENCY + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PORTAL_SAMPLES + light_id + 2, state)

    def set_sky(self, dialog, light_id, state):
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_MULTIPLIER + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_SUN_DISK_SCALE + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_HAZE + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_OZONE + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_HORIZON_HEIGHT + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_REDBLUESHIFT + light_id + 2, state)
        dialog.Enable(const.REDSHIFT_LIGHT_PHYSICALSUN_SATURATION + light_id + 2, state)

    def disable_redshift_data(self, dialog, list_lights, layers):
        for i in xrange(len(list_lights)):
            light_type = dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_LIGHT_TYPE + i + 2)

            #AREA, POINT, SPOT, INFINITE
            if light_type in [3, 1, 2, 0]:

                #Si color
                if dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_COLORMODE + i + 2):
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLOR + i + 2, False)
                else:
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_TEMP + i + 2, False)

                #Unit type
                if dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_UNIT + i + 2) not in [3, 4]:
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LUMEN + i + 2, False)

                #Area
                if light_type == 3:
                    geo_type = dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_UNIT + i + 2)
                    if geo_type == 4:
                        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SIZEX + i + 2, False)
                        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SIZEY + i + 2, False)
                        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_SIZEZ + i + 2, False)

                    elif geo_type in [2, 3]:
                        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_AREA_BIDIRECTIONAL + i + 2, False)

                    self.set_spot(dialog, i, False)
                    self.set_dome(dialog, i, False)
                    self.set_ies(dialog, i, False)
                    self.set_portal(dialog, i, False)
                    self.set_sky(dialog, i, False)

                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_TRANPS + i + 2, False)
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS + i + 2, False)
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE + i + 2, False)

                #Point
                elif light_type == 1:
                    self.set_area(dialog, i, False)
                    self.set_spot(dialog, i, False)
                    self.set_dome(dialog, i, False)
                    self.set_ies(dialog, i, False)
                    self.set_portal(dialog, i, False)
                    self.set_sky(dialog, i, False)

                #Spot
                elif light_type == 2:
                    self.set_area(dialog, i, False)
                    self.set_dome(dialog, i, False)
                    self.set_ies(dialog, i, False)
                    self.set_portal(dialog, i, False)
                    self.set_sky(dialog, i, False)

                #Infinite
                elif light_type == 0:
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DECAY_TYPE + i + 2, False)
                    self.set_area(dialog, i, False)
                    self.set_spot(dialog, i, False)
                    self.set_dome(dialog, i, False)
                    self.set_ies(dialog, i, False)
                    self.set_portal(dialog, i, False)
                    self.set_sky(dialog, i, False)

                #Dome

            #DOME
            elif light_type == 4:
                self.set_area_point_spot_infinite(dialog, i, False)
                self.set_area(dialog, i, False)
                self.set_spot(dialog, i, False)
                self.set_ies(dialog, i, False)
                self.set_portal(dialog, i, False)
                self.set_sky(dialog, i, False)

                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE + i + 2, False)

            #IES
            elif light_type == 5:
                #Si color
                if dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_IES_COLORMODE + i + 2):
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLOR + i + 2, False)
                else:
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_TEMP + i + 2, False)

                self.set_area_point_spot_infinite(dialog, i, False)
                self.set_area(dialog, i, False)
                self.set_spot(dialog, i, False)
                self.set_dome(dialog, i, False)
                self.set_portal(dialog, i, False)
                self.set_sky(dialog, i, False)

            #PORTAL
            elif light_type == 6:
                self.set_area_point_spot_infinite(dialog, i, False)
                self.set_area(dialog, i, False)
                self.set_spot(dialog, i, False)
                self.set_dome(dialog, i, False)
                self.set_sky(dialog, i, False)

                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE + i + 2, False)

            #SKY
            elif light_type == 7:
                self.set_area_point_spot_infinite(dialog, i, False)
                self.set_area(dialog, i, False)
                self.set_spot(dialog, i, False)
                self.set_dome(dialog, i, False)
                self.set_portal(dialog, i, False)

                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_ENABLE + i + 2, False)


            #Shadow
            if not dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_SHADOW_ENABLE + i + 2) and light_type != 7:
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_TRANPS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE + i + 2, False)

            #Caustic
            if not dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_PHOTON_ENABLED + i + 2):
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_PHOTON_INTENSITY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_PHOTON_NUM + i + 2, False)

            #GI
            if not dialog.GetBool(const.LIGHT_LISTER_REDSHIFT_GI_ENABLED + i + 2):
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_GI_MULITPLIER + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_GI_PHOTONS + i + 2, False)


            if not len(layers):
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LAYERS + i + 2, False)
            else:
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LAYERS + i + 2, True)

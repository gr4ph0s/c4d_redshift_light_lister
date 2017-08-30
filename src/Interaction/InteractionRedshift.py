import c4d

from ..Const import Const
from .InteractionFunction import InteractionFunction

const = Const()
ifc = InteractionFunction()

class InteractionRedshift(InteractionFunction):

    def redshift_interaction(self, dialog, doc, clicked_id, msg, list_lights, layers):
        #Order
        #self.order_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_MIN_MAX, clicked_id, list_lights)
        self.order_interaction_up(dialog, doc, const.LIGHT_LISTER_REDSHIFT_ORDER_UP, clicked_id, list_lights)
        self.order_interaction_down(dialog, doc, const.LIGHT_LISTER_REDSHIFT_ORDER_DOWN, clicked_id, list_lights)

        #Select
        self.selection_interaction(doc, const.LIGHT_LISTER_REDSHIFT_SELECT, clicked_id, msg, list_lights)

        #Name
        self.name_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_NAME, clicked_id, list_lights)

        #enable
        self.enable_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_ENABLE, clicked_id, list_lights)

        #Viewport Change
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_ENABLE_VIEWPORT,
                              clicked_id, list_lights, c4d.ID_BASEOBJECT_VISIBILITY_EDITOR)

        #Render Change
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_ENABLE_RENDER,
                              clicked_id, list_lights, c4d.ID_BASEOBJECT_VISIBILITY_RENDER)

        #Light Type
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_LIGHT_TYPE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_TYPE)

        #Preview
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_PREVIEW,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PREVIEW)

        #Show Illum
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SHOW_ILLUM,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_SHOW_ILLUMINATION)

        #Affects Diffuse
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AFFECT_DIFFUSE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_AFFECTS_DIFFUSE)

        #Affects Specular
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AFFECT_SPECULAR,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_AFFECTS_SPECULAR)

        #Color mode
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_COLORMODE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_COLORMODE)

        #Color
        self.color_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_COLOR,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_COLOR)

        #Temp
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_TEMP,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_TEMPERATURE)

        #Unit
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_UNIT,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_UNITSTYPE)

        #Luminous
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_LUMEN,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_LUMENSPERWATT)

        #Intensity
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_INTENSITY,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_INTENSITY)

        #Decay Type
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DECAY_TYPE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_DECAYTYPE)

        #Area Type
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_GEO,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_GEOMETRY)

        #SizeX
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_SIZEX,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SIZEX)

        #SizeY
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_SIZEY,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SIZEY)

        #SizeZ
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_SIZEZ,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SIZEZ)

        #Visible in Render
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_VISIBLE_RENDER,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_VISIBLE_IN_RENDER)

        #Bidirectional
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_BIDIRECTIONAL,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_BIDIRECTIONAL)

        #Normalize
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_NORMALIZE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_NORMALIZE)

        #Sample
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_AREA_SAMPLES,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_AREA_SAMPLES)

        #Angle
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SPOT_ANGLE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_SPOT_CONE_ANGLE)

        #Faloff angle
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SPOT_FALLOFF,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICAL_SPOT_CONE_FALLOFF_ANGLE)

        #Dome Type
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_ENVTYPE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_ENVTYPE)

        #Exposure Compensation
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_APPLYEXPOSURECOMPENSATION,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_APPLYEXPOSURECOMPENSATION)

        #Exposure
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_EXPOSURE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_EXPOSURE0)

        #Hue
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_HUE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_HUE0)

        #Saturation
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_SATURATION,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_SATURATION0)

        #Tint
        self.color_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_TINT,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_COLOR)

        #Sample
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_DOME_SAMPLE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_DOME_SAMPLES)

        #IES Color mode
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_IES_COLORMODE,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_IES_COLORMODE)

        #IES Color
        self.color_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_IES_COLOR,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_IES_COLOR)

        #IES Temp
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_IES_TEMP,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_IES_TEMPERATURE)

        #IES mult
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_IES_MULT,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_IES_MULTIPLIER)

        #PORTAL sizeX
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PORTAL_SIZEX,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_SIZEX)

        #PORTAL sizeY
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PORTAL_SIZEY,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_SIZEY)

        #PORTAL mult
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PORTAL_MULTIPLIER,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_MULTIPLIER)

        #PORTAL tint
        self.color_interaction(dialog, doc, const.REDSHIFT_LIGHT_PORTAL_TINT_COLOR,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_TINT_COLOR)

        #PORTAL Transparency
        self.color_interaction(dialog, doc, const.REDSHIFT_LIGHT_PORTAL_TRANSPARENCY,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_TRANSPARENCY)

        #PORTAL samples
        self.long_interaction(dialog, doc, const.REDSHIFT_LIGHT_PORTAL_SAMPLES,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PORTAL_SAMPLES)

        #SKY Intensity
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_MULTIPLIER,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_MULTIPLIER)


        #SKY Non Physical
        self.bool_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY,
                              clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_USENONPHYSICALINTENSITY)


        #SKY Disk Scale
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_SUN_DISK_SCALE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_SUN_DISK_SCALE)

        #SKY Haze
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_HAZE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_HAZE)

        #SKY Ozone
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_OZONE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_OZONE)

        #SKY Height
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_HORIZON_HEIGHT,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_HORIZON_HEIGHT)

        #SKY Red-blue shift
        self.float_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_REDBLUESHIFT,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_REDBLUESHIFT)

        #SKY samples
        self.long_interaction(dialog, doc, const.REDSHIFT_LIGHT_PHYSICALSUN_SATURATION,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHYSICALSUN_SATURATION)

        #Vol Contribution
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_VOLUME,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_VOLUME_RAY_CONTRIBUTION_SCALE)

        #Vol Sample
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_VOLUME_SAMPLE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_VOLUME_NUM_SAMPLES)

        #Shadow Enable
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SHADOW_ENABLE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_SHADOW)

        #Shadow Transparecy
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SHADOW_TRANPS,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_SHADOWTRANSPARENCY)

        #Shadow Contribution
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_SAMPLINGOVERRIDES_SHADOWSAMPLESSCALE)

        #Shadow Sample
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_SAMPLINGOVERRIDES_NUMSHADOWSAMPLES)

        #Caustics
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_PHOTON_ENABLED,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_CAUSTICS_ENABLED)

        #Caustics mult
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_PHOTON_INTENSITY,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_CAUSTICS_INTENSITY_MULTIPLIER)

        #Caustic num
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_PHOTON_NUM,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_CAUSTICS_NUM_PHOTONS)

        #GI
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_GI_ENABLED,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_GI_ENABLED)

        #GI mult
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_GI_MULITPLIER,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_GI_INTENSITY_MULTIPLIER)

        #GI num
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_GI_PHOTONS,
                               clicked_id, list_lights, c4d.REDSHIFT_LIGHT_PHOTON_GI_NUM_PHOTONS)

        #layer
        self.layer_interaction(dialog, doc, const.LIGHT_LISTER_REDSHIFT_LAYERS,
                               clicked_id, list_lights, layers)

        self.disable_redshift_data(dialog, list_lights, layers)

        return dialog
        c4d.EventAdd()


    def set_area_point_spot_infinite(self, dialog, light_id, state):

        if state:
            #Si color
            if dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_COLORMODE + light_id + 2):
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLOR + light_id + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_TEMP + light_id + 2, True)
            else:
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_TEMP + light_id + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLOR + light_id + 2, True)

            #Unit type
            if dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_UNIT + light_id + 2) not in [3, 4]:
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LUMEN + light_id + 2, False)
            else:
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LUMEN + light_id + 2, True)

            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLORMODE + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_UNIT + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_INTENSITY + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DECAY_TYPE + light_id + 2, state)
        else:
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_TEMP + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLOR + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_LUMEN + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_COLORMODE + light_id + 2, state)
            dialog.Enable(const.LIGHT_LISTER_REDSHIFT_UNIT + light_id + 2, state)
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
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_APPLYEXPOSURECOMPENSATION + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_EXPOSURE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_HUE + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_SATURATION + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_TINT + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_DOME_SAMPLE + light_id + 2, state)

    def set_ies(self, dialog, light_id, state):
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_PATH + light_id + 2, state)
        dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLORMODE + light_id + 2, state)
        #dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLOR + light_id + 2, state)
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
                self.set_area_point_spot_infinite(dialog, i, True)

                #Area
                if light_type == 3:
                    self.set_area(dialog, i, True)
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
                    self.set_spot(dialog, i, True)

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

            #DOME
            elif light_type == 4:
                self.set_dome(dialog, i, True)
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
                self.set_ies(dialog, i, True)
                #Si color
                if dialog.GetLong(const.LIGHT_LISTER_REDSHIFT_IES_COLORMODE + i + 2):
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLOR + i + 2, False)
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_TEMP + i + 2, True)
                else:
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_TEMP + i + 2, False)
                    dialog.Enable(const.LIGHT_LISTER_REDSHIFT_IES_COLOR + i + 2, True)

                self.set_area_point_spot_infinite(dialog, i, False)
                self.set_area(dialog, i, False)
                self.set_spot(dialog, i, False)
                self.set_dome(dialog, i, False)
                self.set_portal(dialog, i, False)
                self.set_sky(dialog, i, False)

            #PORTAL
            elif light_type == 6:
                self.set_portal(dialog, i, True)
                self.set_area_point_spot_infinite(dialog, i, False)
                self.set_area(dialog, i, False)
                self.set_spot(dialog, i, False)
                self.set_dome(dialog, i, False)
                self.set_sky(dialog, i, False)

                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SOFTNESS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_REDSHIFT_SHADOW_SAMPLE + i + 2, False)

            #SKY
            elif light_type == 7:
                self.set_sky(dialog, i, True)
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
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_exif_data(image_path):
    # Open the image
    img = Image.open(image_path)

    # Extract Exif data
    exif_data = img._getexif()

    if exif_data is not None:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)

            # Check if the tag represents GPS information
            if tag_name == 'GPSInfo':
                gps_info = {}
                for gps_tag, gps_value in value.items():
                    gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                    gps_info[gps_tag_name] = gps_value
                print("GPS Info:", gps_info)
                
            # Check if the tag represents DateTime information
            elif tag_name == 'DateTimeOriginal':
                print("DateTime Original:", value)

def get_dji_meta(image_path):
   
    djimeta=["AbsoluteAltitude","RelativeAltitude","GimbalRollDegree","GimbalYawDegree",\
         "GimbalPitchDegree","FlightRollDegree","FlightYawDegree","FlightPitchDegree"]
    
    # read file in binary format and look for XMP metadata portion
    fd = open(image_path,'rb')
    d= fd.read()
    xmp_start = d.find(b'<x:xmpmeta')
    xmp_end = d.find(b'</x:xmpmeta')

    # convert bytes to string
    xmp_b = d[xmp_start:xmp_end+12]
    xmp_str = xmp_b.decode()
    
    fd.close()
    
    # parse the XMP string to grab the values
    xmp_dict={}
    for m in djimeta:
        istart = xmp_str.find(m)
        ss=xmp_str[istart:istart+len(m)+10]
        val = float(ss.split('"')[1])
        xmp_dict.update({m : val})
        
    return xmp_dict
image_path = 'your_image_path'
get_dji_meta(image_path)
extract_exif_data(image_path)
print(get_dji_meta(image_path))


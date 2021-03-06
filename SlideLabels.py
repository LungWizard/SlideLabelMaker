from PIL import Image, ImageDraw, ImageFont
import qrcode

#DonorID is intended to be 4 characters in length
#The Tissue field is intended to be 3 characters in length
#The Block field is intended to be UP TO 5 characters in length 
#Start and stop fields indicate the first and last slide number

DonorID = "XXXX"
Tissue = "YYY"
Block = "ZZZZZ"
Start = 1
Stop = 3


for X in range(Start,Stop+1):
    #Label settings
    Label = Image.new('RGB', (135, 125), color = (255, 255, 255))
    
    #QR code settings
    QR_Code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2.5,
            border=0,
    )
    
    #Add data to QR code
    QR_Code.add_data(DonorID + '-' + Tissue 
                     + '-' + Block + str(X))

    #Generate QR code
    QR_Image = QR_Code.make_image(fill_color="black", back_color="white")
    
    #Define font and font size
    Arial = ImageFont.truetype('arialbd.ttf', 15)
    
    #Make blank label
    Text = ImageDraw.Draw(Label)
    
    #Add text
    Text.text((5,5), DonorID + '-' + Tissue 
                  + '-' + Block, font = Arial, fill = (0, 0, 0))
    Text.text((110, 95), str(X), font = Arial, fill = (0, 0, 0))

    #Add QR code to label
    Label.paste(QR_Image, box = (80, 40), mask = None)
    
    #Save label as PNG
    Label.save(DonorID + Tissue + Block + str(X)+'.png')
from PIL import Image
import random

def generate_layers():
    #code used to generate different backgrounds
    for i in range(6):
        r=int(random.randint(0,255))
        g=int(random.randint(0,255))
        b=int(random.randint(0,255))
        img = Image.new('RGB',(1280,720),(r,g,b))
        img.save('background/bg{}.png'.format(i))
        
    ls=['body','eyes','face','hair']
    # driver code to remove background
    def convertImage(i,j):
        img = Image.open("{}/{}{}.png".format(j,j,i))
        img = img.convert("RGBA")
    
        datas = img.getdata()
    
        newData = []
    
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append((0, 0, 0, 0))
            else:
                newData.append(item)
    
        img.putdata(newData)
        img.save("{}/{}{}.png".format(j,j,i))

    # driver code to generate different colors for body
    for j in ls:
        for i in range(6):
            img = Image.open("{}/{}.png".format(j,j))
            img = img.convert("RGB")
            d = img.getdata()
            r=int(random.randint(0,255))
            g=int(random.randint(0,255))
            b=int(random.randint(0,255))
            new_image = []
            for item in d:
                if item[0] in list(range(140, 250)):
                    new_image.append((r, g, b))
                else:
                    new_image.append(item)
            img.putdata(new_image)
            img.save("{}/{}{}.png".format(j,j,i))
            convertImage(i,j)

def generate_nft():
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    for e in range(6):
                        bg=Image.open(("background/bg{}.png".format(e))).convert("RGBA")
                        body=Image.open(("body/body{}.png".format(b))).convert("RGBA")
                        eyes=Image.open(("eyes/eyes{}.png".format(c))).convert("RGBA")
                        face=Image.open(("face/face{}.png".format(d))).convert("RGBA")
                        hair=Image.open(("hair/hair{}.png".format(a))).convert("RGBA")
                        text=Image.open(("text/text.png")).convert("RGBA")
                        bg.paste(body,(0,0),body)
                        bg.paste(eyes,(0,0),eyes)
                        bg.paste(face,(0,0),face)
                        bg.paste(hair,(0,0),hair)
                        bg.paste(text,(0,0),text)
                        bg.save("result/nft-{}+{}+{}+{}+{}.png".format(a,b,c,d,e))
if __name__=='__main__':
    generate_layers()
    generate_nft()
    

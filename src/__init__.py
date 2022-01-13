from PIL import Image
import random

def generate_layers():
    
    #code used to generate different backgrounds
    for i in range(6): # 6 different bg are being created
        # for generating random bg colors using rgb code
        r=int(random.randint(0,255))
        g=int(random.randint(0,255))
        b=int(random.randint(0,255))
        img = Image.new('RGB',(1280,720),(r,g,b))
        # saving the final produced background
        img.save('background/bg{}.png'.format(i))
        
    ls=['body','eyes','face','hair']
    
    # driver code to remove background
    '''
     here the colored layers are analysed for blacks and then made
     transparent by replacing all the black pixels with transparent pixels
     which are then saved into their respective folder.
    '''
    def convertImage(i,j):
        img = Image.open("{}/{}{}.png".format(j,j,i))
        img = img.convert("RGBA")
        datas = img.getdata() # gathering color scheme of img
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0: # condition to check blacks
                newData.append((0, 0, 0, 0)) # replacing blacks
            else:
                newData.append(item)
        img.putdata(newData) # updating new pixel information into the img
        img.save("{}/{}{}.png".format(j,j,i)) #saving the final bg removed transparent img

    
    # driver code to generate different colors for layers
    
    '''
     this is the main loop which generates different unique colored layers
     of body,eye,hair,face from provided original file
     png with no 0 indicates the source file from which different colored
     version of it are created with number extensions
    '''
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
            '''
             all the colored layers generated here doesnt have transparent bg
             to make them transparent, they are sent to another function 
             convertImage()
            '''
            convertImage(i,j)

'''
In this function all the layers are stacked on each other creating different combinations
Strictly there is no repetition 
'''
def generate_nft():
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    for e in range(6):
                        '''
                        opening layer one by one respectievely
                        '''
                        bg=Image.open(("background/bg{}.png".format(e))).convert("RGBA")
                        body=Image.open(("body/body{}.png".format(b))).convert("RGBA")
                        eyes=Image.open(("eyes/eyes{}.png".format(c))).convert("RGBA")
                        face=Image.open(("face/face{}.png".format(d))).convert("RGBA")
                        hair=Image.open(("hair/hair{}.png".format(a))).convert("RGBA")
                        text=Image.open(("text/text.png")).convert("RGBA")
                        '''
                         layering each layer on one another
                         to make a single nft
                        '''
                        bg.paste(body,(0,0),body)
                        bg.paste(eyes,(0,0),eyes)
                        bg.paste(face,(0,0),face)
                        bg.paste(hair,(0,0),hair)
                        bg.paste(text,(0,0),text)
                        # saving the nft
                        bg.save("result/nft-{}+{}+{}+{}+{}.png".format(a,b,c,d,e))

if __name__=='__main__':
    generate_layers()
    generate_nft()
    

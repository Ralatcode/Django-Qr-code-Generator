import segno 

# introduction to creating a qr-code with segno python package

t53_qrcode = segno.make("For here??", micro = False)

t53_qrcode.save('qr2.png')

# with segno we can create diff format of the output , i.e 
t53_qrcode.save('qr2.svg')
# use scale paramter in save to  scale up qr code size
t53_qrcode.save('qr3.png', scale=7)

# for colorful qr code use dark and light paramter
#  light is the background and dark are the codes

t53_qrcode.save('new.svg', dark="cyan", light="purple", scale=5, unit="mm")


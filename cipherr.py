




def cipher(message,key,mode):
 letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 translated=''
 message=message.upper()

 for symbol in message:
   if symbol in letters:
       indexx= letters.find(symbol)
       if mode =='encrypt': 
           indexx=indexx+key
       elif mode=='decrypt':
          indexx=indexx-key
       if indexx>=len(letters):
           indexx= indexx-len(letters)
       elif indexx<0:
           indexx=indexx+len(letters)
       translated+=letters[indexx]
   else:
       translated = translated +symbol
 print(translated)
cipher('ZL ANZR VF UHFFRVA',13,'decrypt')
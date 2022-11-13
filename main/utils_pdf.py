import numpy as np
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
import cv2
from PIL import Image
import os
from django.conf import settings

class PDFClass:

      def __init__(self, name, start_page = 2, end_page = -1):
            self.sp = start_page
            self.ep = end_page

            self.name = name
            
      def proc_pdf(self):
            self.pdf_pgs_temp = convert_from_path(self.name)
            self.pdf_pgs_temp = self.pdf_pgs_temp[self.sp:self.ep]
            self.no_pgs = len(self.pdf_pgs_temp)
            self.pdf_pgs = []
            self.pg_idx = 0

            for im in self.pdf_pgs_temp:
                  self.pdf_pgs.append(np.asarray(im))


            return self.pdf_pgs

      def proc_page(self, no=0):
            self.pg_idx = no
            self.fp = self.pdf_pgs[no]
            
            image = self.fp
            # cv2.imshow('img', image)
            # plt.imshow(image)
            result = image.copy()
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,51,9)

            # Fill rectangular contours
            # cv2.imshow('thresh', thresh)
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # print(len(cnts))
            # print(cnts[0])
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            # print(len(cnts))
            # cnts = cnts[0]
            for c in cnts:
                  cv2.drawContours(thresh, [c], -1, (255,255,255), -1)
            # x,y,w,h = cv2.boundingRect(c)
            # cv2.circle(image, (x,y), radius=6, color=(0, 0, 255), thickness=-1)
            
            # cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 10)

            # plt.imshow(thresh)

            # Morph open
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4)

            # cv2.circle(image, (op[0][-1], op[1][-1]), radius=6, color=(0, 0, 255), thickness=-1)
            # Draw rectangles
            # plt.imshow(image)
            cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            # print(len(cnts))
            ji = 0

            if(no == 0):
                  _, _, self.pg_w, self.pg_h = cv2.boundingRect(cnts[0])
                  print(self.pg_h)
            else:
                  _,_,_,h1 = cv2.boundingRect(cnts[0])
                  ns = round(h1/self.pg_h)
                  self.pg_h = round(h1/ns)
            
            
            cards_dir = str(settings.BASE_DIR) + "/cards"

            for c in cnts:
                  x,y,w,h = cv2.boundingRect(c)
                  print(h)
                  if(len(cnts) == 1):
                        for j in range(3):
                              for k in range(10):
                                    wi_p = j*(self.pg_w//3)
                                    hi_p = k*(self.pg_h)

                                    hi = (k+1)*(self.pg_h)
                                    wi = (j+1)*(self.pg_w//3)
                                    # cv2.rectangle(image, (x, y), (x + wi, y + hi), (0,255,0), 3)
                                    # img1 = image[x + wi_p:x + wi, y + hi_p:y+hi]
                                    # if(np.mean(img1[:,:h//5]) < 254):
                                    # print(img1.shape)
                                    img1 = Image.fromarray(image)
                                    img1 = img1.crop((x + wi_p, y + hi_p, x + wi, y + hi))
                                    it = np.asarray(img1)
                                    if(np.mean(it[:, :10]) < 254):
                                          img1.save(cards_dir+f'/img_{self.pg_idx}_{ji}.png')
                                          ji += 1

                        
                  else:    
                        for j in range(3):
                              wi_p = j*(w//3)
                              wi = (j+1)*(w//3)
                              # print(h)
                              # cv2.rectangle(image, (x, y), (x + wi, y + h), (0,255,0), 3)
                              img1 = Image.fromarray(image)
                              img1 = img1.crop((x + wi_p, y, x + wi, y + h))
                              img1.save(cards_dir+f'/img_{self.pg_idx}_{ji}.png')
                              ji += 1

                  # cv2.circle(image, (x,y), radius=6, color=(0, 0, 255), thickness=-1)

      def proc_all(self):
            
            pg_i = 0
            
            self.proc_page(pg_i)

            for pg_i in range(1, self.no_pgs):
                  self.proc_page(pg_i)


            
def main():
      p1 = PDFClass('S06A69P186.pdf')
      p1.proc_pdf()
      p1.proc_page(0)
      p1.proc_page(-1)

      plt.imshow(p1.pdf_pgs[0])
      plt.show()

if __name__ == '__main__':
      main()

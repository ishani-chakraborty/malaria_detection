## Malaria Detection Project

#### This ML project represents my first experience with working with ML models and my first ML project! This project is inspired by a Youtube Project Series that used a similar model to help detect diabetes in at-risk individuals. 

#### This past semester, my friend had her first research experience to study malarial drug resistance. She explained to me how most of her training and research were wet labs, but it instanteously gave me the idea of how undergruate research would benefit from malaria detection tools. 

##### Solution: This would both expedite the process, ensure greater precision and accuracy, and finally limit the margin of error that result from their wet labs. 

##### Problem Statement: I had no access to images or any training data that would help me build a model for malaria detection, and tried to think of ways I could do this. I reached out to my friend regarding any possible digital image processing she could provide for me, however, this wasn't a viable option due to the confidentiality measures of the research deparment.

##### I went ahead and did an extensive amount of digging online and found existing images of organized cell images. They were organized into both Uninfected and Parasitized Cell Images. This gave me a place to start for my model:

#### Image Processing and Model Architechture:
#### 1. Read original images
#### 2. Convert to grayscale
#### 3. Contour detection
#### 4. Get the areas of the 5 largest contours

##### Run ```ruby
              require 'redcarpet'
              markdown = Redcarpet.new("Hello World!")
              puts markdown.to_html
          ```

###### **Feel free to contribute to the repository or contact me for questions and changes!**

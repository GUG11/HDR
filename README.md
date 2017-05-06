<!-- Enable Mathjax -->

<script type="text/x-mathjax-config">
    TeX: {extensions: ["AMSmath.js","AMSsymbols.js","mhchem.js","noErrors.js","noUndefined.js"]},
    MathJax.Hub.Config({
        tex2jax: {
              inlineMath: [ ['$','$'], ['\\(','\\)'] ],   
              preview: ["[math]"],
              displayMath: [ ['$$','$$'] ],
              processEscapes: true         // this allows me to use a literal dollar sign, \$, outside of math mode
    }
});
</script>
<script type="text/javascript" async src="path-to-mathjax/MathJax.js?config=TeX-AMS_CHTML"></script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# High-Dynamic-Range Imaging (UW-Madison CS766 course project)

In this project, we build an HDR imaging software. The project consists of bracket exposure photo captures, radiance estimation and tone mapping. We have not only impelemented the HDR imaging algorithms but also built a complete computer vision systems on an Android phone, including both the image sensing part and the post processing part. We run experiments on a variety of photos from DLSR and Android phones.

## Exposure Estimation
During the image formation procedure of modern digital cameras, the original radiance (illumination of the objects) is nonlinear mapped to the photo. We denote the nonlinear process by function $$f$$, and then the relationship between the scene radiance and the pixel values is
$$ Z_{ij} = f(E_i \Delta t_j) $$

![](files/image_formation.png)
__image source: [1]__


![](files/response_func.png)
![](files/radiance_estimation.png)

## Tone mapping
![](files/rgb_lab.png)
![](files/tonemap.png)
![](files/lab2rgb.png)

## Deploy on Android phones

## [Presentation Slides](files/Zhang.Huayu.slides.pdf)
## Gallary

### DLSR
Big City Lights
![](result/lambda2/Big_City_Lights.jpg)
Raw images:[1](data/Big_City_Lights/Big_City_Lights-ppw-01.jpg) [2](data/Big_City_Lights/Big_City_Lights-ppw-02.jpg) [3](data/Big_City_Lights/Big_City_Lights-ppw-03.jpg) [4](data/Big_City_Lights/Big_City_Lights-ppw-04.jpg)

Izmir Harbor
![](result/lambda2/Izmir_Harbor.jpg)
Raw images:[1](data/Izmir_Harbor/Izmir_Harbor-ppw-01.jpg) [2](data/Izmir_Harbor/Izmir_Harbor-ppw-02.jpg) [3](data/Izmir_Harbor/Izmir_Harbor-ppw-03.jpg) [4](data/Izmir_Harbor/Izmir_Harbor-ppw-04.jpg)  [5](data/Izmir_Harbor/Izmir_Harbor-ppw-05.jpg) [6](data/Izmir_Harbor/Izmir_Harbor-ppw-06.jpg) 

Big City Lights
![](result/lambda2/High_Five.jpg)
Raw images:[1](data/High_Five/High_Five-ppw-01.jpg) [2](data/High_Five/High_Five-ppw-02.jpg) [3](data/High_Five/High_Five-ppw-03.jpg) [4](data/High_Five/High_Five-ppw-04.jpg) [5](data/High_Five/High_Five-ppw-05.jpg) [6](data/High_Five/High_Five-ppw-06.jpg) [7](data/High_Five/High_Five-ppw-07.jpg) [8](data/High_Five/High_Five-ppw-08.jpg)

Big City Lights
![](result/lambda2/The_Marble_Hall.jpg)
Raw images:[1](data/The_Marble_Hall/The_Marble_Hall-ppw-01.jpg) [2](data/The_Marble_Hall/The_Marble_Hall-ppw-02.jpg) [3](data/The_Marble_Hall/The_Marble_Hall-ppw-03.jpg) [4](data/The_Marble_Hall/The_Marble_Hall-ppw-04.jpg) [5](data/The_Marble_Hall/The_Marble_Hall-ppw-05.jpg) [6](data/The_Marble_Hall/The_Marble_Hall-ppw-06.jpg)

Source image credits: <http://farbspiel-photo.com/learn/hdr-pics-to-play-with>
### Android phones
UW-Madison CS basement
![](result/android/IMG_20170420_220249_HDR.jpg)
Raw images:[1](result/android/IMG_20170420_220249_EXP0.jpg) [2](result/android/IMG_20170420_220249_EXP1.jpg) [3](result/android/IMG_20170420_220249_EXP2.jpg)

UW-Madison CS Department
![](result/android/IMG_20170422_124742_HDR.jpg)
Raw images:[1](result/android/IMG_20170422_124742_EXP0.jpg) [2](result/android/IMG_20170422_124742_EXP1.jpg) [3](result/android/IMG_20170422_124742_EXP2.jpg)

UW-Madison W Dayton St in south of CS
![](result/android/IMG_20170421_191455_HDR.jpg)
Raw images:[1](result/android/IMG_20170421_191455_EXP0.jpg) [2](result/android/IMG_20170421_191455_EXP1.jpg) [3](result/android/IMG_20170421_191455_EXP2.jpg)

## References
<ol>
    <li> Paul E Debevec and Jitendra Malik. “Recovering high dynamic range radiance
maps from photographs”. In: ACM SIGGRAPH 2008 classes. ACM. 2008, p. 31.</li>
    <li> Karel Zuiderveld. “Graphics Gems IV”. In: ed. by Paul S. Heckbert. San Diego, CA, USA: Academic Press Professional, Inc., 1994. Chap. Contrast Limited Adaptive Histogram Equalization, pp. 474–485. isbn: 0-12-336155-9.</li>
</ol>

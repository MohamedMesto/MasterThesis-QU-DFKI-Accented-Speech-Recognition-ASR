<table border=0>
<tr border=0>
<td> <img align="left"  alt="Mohamed Mesto" width="100px" height='60px' src="https://github.com/MohamedMesto/MohamedMesto/blob/main/Images/QU-Lab.png"/> </td>
  <td align="center"> <h5><a href="https://www.dfki.de/web">
Deutsches Forschungszentrum für Künstliche Intelligenz
</a><br>German Research Center for Artificial Intelligence<br><a href="https://www.qu.tu-berlin.de/menue/qu/">Institut für Softwaretechnik und Theoretische Informatik<br> 
Quality and Usability Lab</a></h5> </td>
  <td>  <img align="right"  alt="Mohamed Mesto" width="160px" height='60px' src="https://www.dfki.de/fileadmin/user_upload/DFKI/Medien/Logos/Logos_DFKI/DFKI_Logo.png"/></td>
</tr>
<tr border=0>
<td> </td><td  align="center"><h5> Thesis Topic </h5> </td><td> </td>
</tr>
<tr border=0>
<td> </td> <td align="center"><h5><a href="https://github.com/fraunhoferfokus">"Accented Speech Recognition"</a></h5> </td><td> </td>
</tr>
  <tr>
    <td> </td>
<td align="center">Supervisors</td>
    <td> </td>
</tr>
  <tr>
    <td> </td>  <td align="center"><a href="https://www.qu.tu-berlin.de/v-menue/team/professur/">	Prof. Dr. Sebastian Möller</a> </br><a href="https://www.linkedin.com/in/tim-polzehl-45a10a36/"> Dr. Tim Polzehl    </a></td>
      <td align="center"></td>
    
</tr>
</table>

# MasterThesis: Accented Speech Recognition
 
## Abstract

In this study, we conduct a comprehensive analysis of how accent information influences the internal representation of speech in an end-to-end automatic speech recognition (ASR) system. Our approach involves utilizing the state-of-the-art Conformer-Transducer-Large model as the basis for our ASR system. This model architecture combines convolutional neural networks (CNNs) with transformers, enabling effective capturing of both local and global dependencies within the input audio data.

To train the model, we initialize it with a large amount of US-accented English speech data and subsequently fine-tune it on a vast quantity of DE-accented German speech data. We evaluate the performance of the model on speech samples representing eleven distinct German accents. To investigate the impact of accents on the internal representation, we employ two primary probing techniques: a) Gradient-based explanation methods and b) Analysis of the outputs from accent and phone classifiers.

Our findings reveal consistent trends across different accents, irrespective of the probing technique employed. Moreover, we observe that the initial convolutional layer encodes the majority of accent-related information. This observation suggests possibilities for adapting the end-to-end model to learn representations that are invariant to accents.

Overall, our study offers a detailed examination of how accents are manifested in the internal representation of speech within an end-to-end ASR system.

## keywords
Accented speech recognition, accent recognition, acoustic modeling, end-to-end ASR

## Contributors
- Mohamed Mesto m.mesto@campus.tu-berlin.de  , Mohamedmesto111@gmail.com


## License & copyright
© Mohamed Mesto
License under the [MIT License] (LICENSE).

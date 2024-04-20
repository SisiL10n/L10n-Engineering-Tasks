Scenario-based task 1: Parse XML

A new client is sending us a XML for translation into 11 languages. Although your company has translated several types of XML in the past, this one is a little bit tricky. For one thing, the client is asking only for a “partial” translation. Only items whose “name” property is an even number value should be translated. For example, the string with “name=’num6’” needs to be translated, while the string with “name=’num1’” does not.

Your project manager is asking for a solution. Now she is under the impression that she herself must copy and paste all the strings to a spreadsheet, have a linguist translate them, and incorporate them back. But she is not quite happy doing that. She thought this approach would be quite risk-leaning and ineffective. This is a document that has 19 strings for translation, which is fairly easy to handle. But what if sometime in the future the client sends you a document with 190 or even 1900  such strings?

Also, your project manager had a loose memory of how they did things in the past. She told you that the last engineer, who left the company one year ago, used to have a filter set up in the CAT tool that would only import XML items with a “class=’NEED’” property. Any item without the “class=’NEED’” would not be imported. This filter seems to be still functioning well in your CAT tool. 

Task Description:

1)	Prep the document for translation in a CAT-tool WITHOUT manually copying and pasting things around.
2)	Regarding what the project manager told you about the old filter, it is your call whether to use it. The project manager thought it might make your work easier, but if you have a better solution surely you can go the other way. 
3)	After the file prep step, pseudo translate (Or use machine translation) your XML into Traditional Chinese, and generate the result.
4)	If you decide to use the old filter, you can skip task 3) because the system itself will take care of the rest.
5)	If your solution involves a script/program, feel free to attach.
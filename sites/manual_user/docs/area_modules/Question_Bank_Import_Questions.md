# Question Bank: Import Questions {: #question_bank_import}

There are three ways to import QTI 2.1 questions into the question pool using the import button.

![Question Import](assets/question_import_options.png)

  *  **ZIP-file** from local computer: Choose this option if you have a set of questions or a test as .zip-file.
  *  **Tests from authoring area**: Select the test you want to import from the available learning resources. To do this, click on the "Import learning resource" link in the corresponding line. All questions of the selected learning resource are imported directly into the question pool. 
  * QTI 2.1 **Excel import** via copy&paste: Prepare the questions in the "template excel import" you can find in the import wizard. When you are finished creating your questions in the Excel file, select the the questions in Excel and copy&paste them to the input field.

### Usage of the file "Excel Import Template"   

Start the Excel import via Copy&Paste and download the Excel import template. It forms the basis for your further procedure.

The question import via Excel files allows you to import multiple questions at once in simple way. The import of excel questions can for example be used to import questions from other systems when the questions do also support the QTI 2.1 standards. 

The Excel template contains four columns:

a) Keyword/Score: Aspect at issue

b) Value: the desired value or text

c) Extra: Extra information

d) Explanation: Further explanations, e.g. whether this element is optional.

The template contains information for importing the following question types:
* FIB (Fill in the blank)
* Numerical 
* MC (Multiple Choice)
* Inlinechoice 
* SC (Single Choice)
* KPRIM
* Essay 
* Matrix
* Drag&Drop
* Truefalse

The questions are each listed one below the other with a separator line. When copying, Excel or a similar program such as OpenOffice or Numbers converts the data into a comma-separated text.

The options for the question types contained in the template are presented below:

#### Multiple-choice question

 **type**|MC for multiple-choice  
---|--- 
 **title**|Title of the question / topic    
 **question**|The question text. Minimal HTML formatting is allowed.   
 **max. answers**|  Max. number of possible answers.  
 **min. answers**|  Min. number of possible answers.  
 **points**|The maximal score. The minimal score is always set to 0.  
  
You can create as many answers as you like, each in a separate line. The point values for the individual answers can also be defined, e.g.

![MC_Import_Beispiel](assets/MC_import_Beispiel.png )  

#### Single-choice question


 **type**| SC für Single-Choice    
---|---  
 **title**|Title of the question / topic    
 **question**|The question text. Minimal HTML formatting is allowed.    
 **points**|The maximal score. The minimal score is always set to 0.
 **Points when this option is selected, e.g. "1" (correct) or "-1" (incorrect)**| Options text. You can have as many options as you like, each on a separated line with a "0" or "1" point configuration  
  

#### Fill-in-blank (gap) question

 **type**|FIB for fill-in-blank  
 ---|---
 **title**|Title of the question / topic
  **points**|The maximal score. The minimal score is always set to 0.
  **text**| A text element  
 **Points when the gap is correctly answered, e.g. "1"**|Correct answer in a gap. Synonyms can be entered separated with ";". Size of the gap and the maximum characters that can be entered is configured, e.g. "10,8".  


#### Numerical Input

 **type**| Numerical Input
---|---
 **title**|Title of the question / topic
 **points**|The maximal score. The minimal score is always set to 0.
 **text**|  A text element, the question
 **Points when the gap is correctly answered, e.g. "1"**|Correct answer in a gap. Synonyms can be entered separated with ";". 

 Example:

![Numerische Eingabe Import Beispiel](assets/Numerical_Import_Beispiel.png) 


#### Gap with dropdown

 **type**|Inlinechoice for gab with dropdown
---|---
 **title**|Title of the question / topic
 **Question** | The question text.
 **points**| The maximal score. The minimal score is always set to 0.
 **text**|  Text elements with further parts for the question or texts before and after the gaps.
 **Points when the gap is correctly answered, e.g. "1"**|The optional answers of the dropdown list seperated. The correct answer is entered in the following column.
  
 Example:

![Lückentext mit Dropdown Import Beispiel](assets/Inlinechoice_Import_Beispiel.png)


#### KPRIM question

 **type**|  KPRIM  
---|---  
 **title**|  Title of the question / topic  
 **question**|  The question text. Minimal HTML formatting is allowed.  
 **points**|  The maximal score. The minimal score is always set to 0.  
+| Correct answer  
-| Incorrect answer 
-| Incorrect answer  
+| Correct answer
 
Correct answers are therefore marked with **+** and incorrect answers with **-**.


#### Essay question

 **type**|  ESSAY  
---|---  
 **title**|  Title of the question / topic  
 **question**|  The question text. Minimal HTML formatting is allowed.  
 **points**|  The maximal score. The minimal score is always set to 0.  
 **min**|  Minimum word count  
 **max**|  Maximum word count  
  
  

#### MATCH question

 **type**|  MATCH 
---|---
 **title**|  Title of the question / topic  
 **question**|  The question text. Minimal HTML formatting is allowed.  
 **points**|  The maximal score. The minimal score is always set to 0.  
  
The matrix itself is distributed across the columns and rows. The corresponding points are entered in the appropriate field. Here is an example with 3 columns and 3 rows:

![Matrix_Import_Beispiel](assets/Matrix_Import_Beispiel.png) 

  
#### Drag and Drop question

 **type**| Drag & drop  
---|---
 **title**|  Title of the question / topic  
 **question**|  The question text. Minimal HTML formatting is allowed.  
 **points**|  The maximal score. The minimal score is always set to 0.

The implementation in the Excel template is similar to Matrix questions and is spread over several columns and rows. The corresponding points are entered in the appropriate field. Here is an example with 3 columns and 3 rows:  
  
![Drag and Drop Import_Beispiel](assets/dad_Import_Beispiel.png)    
  
#### TrueFalse question

 **type**|  Truefalse  
---|---
 **title**|  Title of the question / topic  
 **question**|  The question text. Minimal HTML formatting is allowed.  
 **points**|  Maximum achievable score. The minimum score is 0.

 Column **unanswered**: Points that are awarded or deducted if no decision is made by the user.

Column **Right**: Points awarded when the answer "Right" is selected by the user.

Column **Wrong**: Points awarded if the answer "False" is selected by the user.

Example:

![True False Import_Beispiel](assets/truefalse_Import_Beispiel.png) 
  
!!! info  

    In addition to the listed fields, there are other optional fields such as "Topic", "Keywords", "License", etc. For more details, see the Excel import template provided as part of the import process.


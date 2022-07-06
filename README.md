# dfs and bfs Simulator
 
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Technologies
 * Project Description
   * Main Page
   * Given Graph
   * Bfs Ouput
   * Dfs Ouput
* How to Run the Project
* To Be Noted
* Credits


INTRODUCTION
------------

  Hi 👋, Myself Navin Praanav and this wibsite is about depth first search and breath first search simulator.
  
  
TECHNOLOGIES
------------

A list of technologies used within the project:
* [HTML](https://en.wikipedia.org/wiki/HTML) :Frontend
* [CSS](https://en.wikipedia.org/wiki/CSS) :Frontend
* [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript) :Frontend
   * [Mermaid-js](https://mermaid-js.github.io/mermaid/#/)
* [Python](https://en.wikipedia.org/wiki/JavaScript) :Backend
* [Flask](https://en.wikipedia.org/wiki/JavaScript) :Backend


PROJECT DESCRIPTION
------------

### MAIN PAGE
  
  ![image](https://user-images.githubusercontent.com/91049629/177582589-dd17ffa1-8574-49df-ba8c-a31475911001.png)


  
### GIVEN GRAPH
  
  ![image](https://user-images.githubusercontent.com/91049629/177582930-7e796aea-fd2d-4d1f-a1b6-8e25dc9e352d.png)


### BFS OUPUT
 
  ![image](https://user-images.githubusercontent.com/91049629/177583080-b1b43f25-0558-4965-8361-a0cb8ff9e765.png)

  
### DFS OUPUT
 ![image](https://user-images.githubusercontent.com/91049629/177585003-dcfbaa72-1aa0-4c56-bd1e-993829cccba2.png)
  


HOW TO RUN THE PROJECT
------------
* **STEP 1** - Enter the size of the adjacency matrix and starting vertex.**Row** input indicates height and **Column** input indicates width of the adjacency matrix. 
![image](https://user-images.githubusercontent.com/91049629/177589898-e8481a1a-1b43-412a-b274-a179efd09751.png)
* **STEP 2** - Click insert
![image](https://user-images.githubusercontent.com/91049629/177590206-a81b88bf-5037-40d4-9a9e-67f3473264f9.png)

* **STEP 3** - A table will be created. On clicking the table enter either 1 or 0 ~(default 0)~.**Example:** If there exist a connect between a vertex 1 and 2 then add 1 to the table cell where the row is 1 and the column is 2.
![image](https://user-images.githubusercontent.com/91049629/177590388-f59f473e-8462-499a-b870-6f71a15d4b48.png)

* **STEP 4** - Click add.
![image](https://user-images.githubusercontent.com/91049629/177590469-a46e5897-3e09-4a24-970b-ecebbe74aa49.png)

* **STEP 5** - To the give adjacency matrix graph will be created.
![image](https://user-images.githubusercontent.com/91049629/177590588-0f78048b-c880-4654-bada-0cb57a433a46.png)

* **STEP 6** - Either click on dfs or bfs button to see the ouput.
   * DFS OUPUT
   ![image](https://user-images.githubusercontent.com/91049629/177590790-a625d179-a495-43d0-ab0a-f1d34decff84.png)

   * BFS OUPUT
   ![image](https://user-images.githubusercontent.com/91049629/177590868-a8b191fc-c8bf-4684-ba48-0542d09829c7.png)


TO BE NOTED
------------

### Used Mermaid-js to achieve graph
Mermaid is a JavaScript based diagramming and charting tool that uses Markdown-inspired text definitions and a renderer to create and modify complex diagrams.
  ``` Mermaid-js
      flowchart TB
        A --> C
        A --> D
        B --> C
        B --> D
  ```
  
CREDITS
------------
A special shout-out to **Kaushik** for working with me in this project.

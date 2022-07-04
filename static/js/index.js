function validateform(){  
    var row=document.getElementById("row").value;  
    var column=document.getElementById("column").value; 
    let r1=Number(row)
    let c1=Number(column)
    if(isNaN(r1) || isNaN(c1)){  
      alert("Not A number ");  
      return false;  
      }
    else if (row==null || row=="" || column=="" || column==null ){  
      alert("Enter Valid input"); 
      return false;  
    }else if(r1<1|| c1<1){  
      alert("No negative or zero is allowed");  
      return false;  
      }  
      else if(r1>=8|| c1>=8){  
        alert("Size too big");  
        return false;  
        }
        
    }  

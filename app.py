from flask import Flask,request,render_template,redirect,url_for
from algo import *
app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    t1=request.form.get('row')
    t2=request.form.get('column')
    arr=list(range(int(t1)))
    arr2=list(range(int(t2)))
    t=True
    return render_template('index.html',arr=arr,arr2=arr2,t=t,t1=t1,t2=t2)

@app.route('/matrix/<t1>/<t2>',methods=['POST'])
def matrix(t1,t2):
    matrix=[]
    for i in range(0,int(t1)):
        temp=[]
        for j in range(0,int(t2)):
            col=request.form.get('index%d%d'%(i,j))
            try: 
                col=col.strip()
                if len(col)==0 or col=='':
                    raise Exception("")
                if col in ['1','0']:
                    temp.append(int(col))
                    
            except Exception as e:
                # print('----IGNORE ',e)
                if col=='':
                    temp.append(0)
                else:
                    m=int(col)>1
                    y=int(col)<0
                    if m or y:
                        return render_template('warning.html')
                    else:
                        pass
        matrix.append(temp)
    print(matrix)
    bfs=bfs_ouptut(matrix,start=0,visited=[])
    dfs=dfs_ouptut(matrix,start=0,visited=[])
    return  render_template('output.html',output1=dfs,output2=bfs)
if __name__=='__main__':
    app.run()
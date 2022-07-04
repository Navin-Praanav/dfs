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
    try:
        arr=list(range(int(t1)))
        arr2=list(range(int(t2)))
    except:
        return render_template('index.html',flash_message="True")
    try:
        if t1<=0 or t2<=0:
            raise Exception("")
    except:
        pass
    t=True
    start=request.form.get('start')
    return render_template('index.html',arr=arr,arr2=arr2,t=t,t1=t1,t2=t2,start=start)

@app.route('/matrix/<t1>/<t2>',methods=['POST'])
def matrix(t1,t2):
    start=0
    matrix=[]
    graph=[]
    for i in range(0,int(t1)):
        temp=[]
        for j in range(0,int(t2)):
            col=request.form.get('index%d%d'%(i,j))
            if col=='1':
                graph.append([i,j])

            try: 
                col=col.strip()
                if len(col)==0 or col=='':
                    raise Exception("")
                if col in ['1','0']:
                    temp.append(int(col))
                else:
                    raise Exception("")
                    
            except Exception as e:
                if col=='':
                    temp.append(0)
                else:
                    try:
                        m=int(col)>1
                        y=int(col)<0
                        print(m,y,temp)
                        if m or y:
                            return render_template('index.html',flash_message="True")
                        else:
                            pass
                    except:
                        return render_template('index.html',flash_message="True")
        matrix.append(temp)
    print(matrix)
    try:
        start=int(request.form.get('start'))
        if start>len(matrix) and start>=0:
            raise Exception("")
    except:
        start=0
    s=0
    for i in matrix:
        s+=sum([int(i) for i in i])
    if s==0:
        return render_template('index.html',flash_message2="True")
    bfs=bfs_ouptut(matrix,start=start,visited=[])
    dfs=dfs_ouptut(matrix,start=start,visited=[])
    return  render_template('output.html',output1=dfs[0],output2=bfs[0],graph=graph,output_dfs=dfs[1],output_bfs=bfs[1])

@app.route('/dfs/<output1>/<output_dfs>')
def dfs(output1,output_dfs):
    try:
        output1=[int(i) for i in output1[1:-1].split(',') if len(i)!=0]
        return render_template('output_dfs.html',output1=output1,output_dfs=output_dfs)
    except Exception as e:
        return render_template('output_dfs.html',flash_message="True")
    

@app.route('/bfs/<output2>/<output_bfs>')
def bfs(output2,output_bfs):
    try:
        output2=[int(i) for i in output2[1:-1].split(',') if len(i)!=0]
        return render_template('output_bfs.html',output2=output2,output_bfs=output_bfs)
    except Exception as e:
        return render_template('output_bfs.html',flash_message="True")
    

if __name__=='__main__':
    app.run(debug=True)
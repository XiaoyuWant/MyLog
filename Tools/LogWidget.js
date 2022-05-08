// CHANGE ME FIRST
let URL="http://HOST:1140/get"

let msgs=await getMSG()
let widget=createWidget()
Script.setWidget(widget)
Script.complete()

function createWidget(){
  let w=new ListWidget()
  
  // 设置刷新频率，一分钟
  let refresh=Date.now()+1000*30
  w.refreshAfterDate=new Date(refresh)
  // 背景色
  w.backgroundColor=new Color("#300927")

  
  
  // 标题
  let caption=w.addText("Logger")
  caption.font=Font.heavyRoundedSystemFont(20)
  caption.textColor=Color.orange()
  let st=w.addStack()
  st.layoutHorizontally()
  
  let tx=st.addText("udt:")
  tx.font=Font.blackRoundedSystemFont(14)
  tx.textColor=Color.white()
  let d=st.addDate(new Date())
  d.applyTimerStyle()
  d.font=Font.blackRoundedSystemFont(14)
  d.textColor=Color.white()
   // 对话内容
  for(i=0;i<msgs.length;i++){
    var item=w.addText(msgs[i])
    item.font=new Font("menlo",14)
    item.textColor=new Color("#ffffff")
    item.minimumScaleFactor=1
    w.addSpacer(3)
  }
  w.presentLarge()
  return w
}

async function getMSG(){
  var lines=[]
  let req =new Request(URL)
  let res= await req.loadJSON();
  let result=res["result"]
  for(i=0;i<result.length;i++){
    var item=result[i]["msg"]
    console.log(item)
    lines.push(item)
  }
  
  return lines
}

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';
import 'package:screen/screen.dart';
import 'LaunchUrl.dart';

class Iframeapp extends StatefulWidget {
    final String text;
    Iframeapp({Key key, @required this.text}) : super(key: key);
  @override
  _IframeappState createState() => _IframeappState(text:text);
}
class _IframeappState extends State<Iframeapp>
{
  Timer timer;

  // bool _isKeptOn = false;
  // double _brightness = 1.0;
    @override
  void initState() {
    initPlatformState();
    super.initState();
  }
    final String text;
    _IframeappState({@required this.text});
  InAppWebViewController webView;
  String url = "";
  double progress = 0;

  @override
void dispose() {
  timer?.cancel();
  Screen.setBrightness(0.5);
  super.dispose();
}

initPlatformState()  {
    setState(() { 
    Screen.setBrightness(0.5);
    {
    if(timer?.isActive != true)
        {      
          timer = Timer.periodic(Duration(minutes: 5), (Timer t) => disScreen());
        }
    }
    });
  }
  disScreen(){
      // if (brightness != 0.0)
      // {
        Screen.setBrightness(0.0);
        timer?.cancel();

    }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
            debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('PHATTIEN',style: const TextStyle(fontSize: 20.0,color: Colors.white,)),
          backgroundColor: Colors.red,
          centerTitle: true,
        ),
        body: 
         GestureDetector(
          behavior: HitTestBehavior.translucent,
          onTap: () =>initPlatformState(),
          child:
        Container(
          child: Column(children: <Widget>[
            Container(
                padding: EdgeInsets.all(0.0),
                child: progress < 1.0
                    ? LinearProgressIndicator(value: progress)
                    : Container()),
            Expanded(
              child: Container(
                margin: const EdgeInsets.all(0.0),
                decoration:
                    BoxDecoration(border: Border.all(color: Colors.white)),
                child: InAppWebView(
                  initialUrl: this.text,
                  initialHeaders: {},
                  initialOptions: InAppWebViewGroupOptions(
                    
                    crossPlatform: InAppWebViewOptions(
                        debuggingEnabled: true,
                    )
                  ),
                  onWebViewCreated: (InAppWebViewController controller) {
                    webView = controller;
                  },
                  onLoadStart: (InAppWebViewController controller, String url) {
                    setState(() {
                      this.url = text;
                    });
                  },
                  onLoadStop: (InAppWebViewController controller, String url)  {
                    setState(() {
                      this.url = text;
                    });
                  },
                  onProgressChanged: (InAppWebViewController controller, int progress) {
                    setState(() {
                      this.progress = progress / 100;
                    });
                  },
                ),
              ),
            ),
            ButtonBar(
              alignment: MainAxisAlignment.center,
              children: <Widget>[
                RawMaterialButton(
                  child: Icon(Icons.home,size: 35.0,),
                  onPressed: () {

                        Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => LaunchUrlDemo()),
                      );
                  },
                   elevation: 2.0,
                    fillColor: Colors.white,
                      padding: EdgeInsets.all(10.0),
                      shape: CircleBorder(),
                      
                ),
              ],
            ),
        ])),),
      ),
    );
  }
}
//

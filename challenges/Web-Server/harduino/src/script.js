var code = 
String.raw`<?php

include "vendor/autoload.php";

try {

    /* Display message */
    $message = "Hello World !";

    /* If custom message is sent, use it instead */
    if (isset($_GET["message"])) {
        $custom = $_GET["message"];
        $message = preg_replace("/^.*$/e", "\"$custom\"", $message);
    }

    /* Twig template loader */
    $loader = new Twig\Loader\FilesystemLoader('./template');
    $twig = new Twig\Environment($loader);
    $template = $twig->load('arduino.html');

    /* Render template */
    echo $template->render(array(
        'message' => $message,
    ));

} catch (Exception $e) {
    die ('ERROR: ' . $e->getMessage());
}

?>`

let split;
  function initSplitPane(){

    //The trick is to destroy the split instance each time the screen is resized so that the previous measurements are overwritten

    if(split){
      split.destroy()
    }
    if(window.innerWidth < 768){
      split = Split(['#editor', '#console'], {
         sizes: [50,50],
         direction: 'vertical',
         cursor: 'row-resize'
       })  
    }
    else{
      split = Split(['#editor', '#console'], {
        sizes: [50,50],
        direction: 'horizontal',
        cursor: 'col-resize'
      })
    }
  }

  function onResize(){
    initSplitPane();
  }


  function initEditor() {
      let editorElement = document.getElementById("editor")
      let consoleElement = document.getElementById("console")
      let panelElement = document.getElementById("panel")
      if (editorElement) {
          let editor = ace.edit("editor");
          // enable autocompletion and snippets
          let mode = editorElement.getAttribute("data-mode") || 'plain_text'
          // Default value is the first one in comments
          // All options are set to default value
          editor.setOptions({
            // editor options
            selectionStyle: 'line',// "line"|"text": 
            highlightActiveLine: true, // boolean: 
            highlightSelectedWord: true, // boolean:
            readOnly: true, // boolean: true if read only
            cursorStyle: 'ace', // "ace"|"slim"|"smooth"|"wide":
            mergeUndoDeltas: true, // false|true|"always":
            behavioursEnabled: true, // boolean: true if enable custom behaviours
            wrapBehavioursEnabled: true, // boolean:
            autoScrollEditorIntoView: undefined, // boolean: this is needed if editor is inside scrollable page
            keyboardHandler: null, // function: handle custom keyboard events

            // renderer options
            animatedScroll: false, // boolean: true if scroll should be animated
            displayIndentGuides: false, // boolean: true if the indent should be shown. See 'showInvisibles'
            showInvisibles: false, // boolean -> displayIndentGuides: true if show the invisible tabs/spaces in indents
            showPrintMargin: false, // boolean: true if show the vertical print margin
            printMarginColumn: 80, // number: number of columns for vertical print margin
            printMargin: undefined, // boolean | number: showPrintMargin | printMarginColumn
            showGutter: true, // boolean: true if show line gutter
            fadeFoldWidgets: false, // boolean: true if the fold lines should be faded
            showFoldWidgets: true, // boolean: true if the fold lines should be shown ?
            showLineNumbers: true,
            highlightGutterLine: false, // boolean: true if the gutter line should be highlighted
            hScrollBarAlwaysVisible: false, // boolean: true if the horizontal scroll bar should be shown regardless
            vScrollBarAlwaysVisible: false, // boolean: true if the vertical scroll bar should be shown regardless
            fontSize: 16, // number | string: set the font size to this many pixels
            fontFamily: undefined, // string: set the font-family css value
            maxLines: undefined, // number: set the maximum lines possible. This will make the editor height changes
            minLines: undefined, // number: set the minimum lines possible. This will make the editor height changes
            maxPixelHeight: 0, // number -> maxLines: set the maximum height in pixel, when 'maxLines' is defined. 
            scrollPastEnd: 0, // number -> !maxLines: if positive, user can scroll pass the last line and go n * editorHeight more distance 
            fixedWidthGutter: false, // boolean: true if the gutter should be fixed width
            theme: 'ace/theme/ambiance', // theme string from ace/theme or custom?

            // mouseHandler options
            scrollSpeed: 2, // number: the scroll speed index
            dragDelay: 0, // number: the drag delay before drag starts. it's 150ms for mac by default 
            dragEnabled: true, // boolean: enable dragging
            focusTimout: 0, // number: the focus delay before focus starts.
            tooltipFollowsMouse: true, // boolean: true if the gutter tooltip should follow mouse

            // session options
            firstLineNumber: 1, // number: the line number in first line
            overwrite: false, // 
            newLineMode: 'auto',
            useWorker: true, // true if use web worker for loading scripts
            useSoftTabs: true, // boolean: true if we want to use spaces than tabs
            tabSize: 4,
            wrap: false, // boolean | string | number: true/'free' means wrap instead of horizontal scroll, false/'off' means horizontal scroll instead of wrap, and number means number of column before wrap. -1 means wrap at print margin
            indentedSoftWrap: true,
            foldStyle: 'markbegin', // enum: 'manual'/'markbegin'/'markbeginend'.
            mode: `ace/mode/${mode}`, // string: language mode 
            enableBasicAutocompletion: true,
            enableSnippets: false,
            enableLiveAutocompletion: true
          });

          //Callback triggered after the theme loads, fetch the CSS properties of the editor only after the theme has loaded
          editor.setTheme("ace/theme/monokai", ()=>{
            let bgColor = getComputedStyle(editorElement)['background-color']
            consoleElement.style.backgroundColor = bgColor
            // panelElement.style.backgroundColor = bgColor
          });

          var seekStart = {
            row: 0,
            column: 0
          };

          editor.session.insert(seekStart, code);

          return editor;
      }
  }

  initSplitPane();
  let editor = initEditor();

  document.getElementById("download").addEventListener("click", ()=>{
    var file = new File([editor.getValue()], "zup.js", {type: "text/plain;charset=utf-8"});
    saveAs(file);
  })
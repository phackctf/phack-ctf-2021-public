<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Agenda</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.18.1/dist/bootstrap-table.min.css">
    <link rel="stylesheet" href="css/main.css" />
    <link rel="icon" href="images/favicon.ico" />
  </head>

  <body>
    <a href="/login.php"><button type="button" class="btn btn-primary" id="login">Se connecter</button></a>

    <div class="title">Agenda</div>
    <div id="tables">
      <div class="subtitle">Listes des conférences</div>
      <table id="table-conferences"></table>

      <div class="subtitle" id="subTalks">Listes des présentations</div>
      <div  id="confName"></div>
      <table id="table-talks"></table>
    </div>

    <!-- Modal -->
    <div id="speakerModal" class="modal fade" role="dialog">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title"></h4>
          </div>
          <div class="modal-body" style="">
            <img id="profilePhoto" src="./images/profile.jpg" />

            <div style="float:right; padding-top: 50px; font-size: 1.8rem;">
              <span id="profileName"></span><br/>
              <span id="profileGithub"></span><br/>
              <span id="profileBlog"></span>
            </div>

          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Fermer</button>
          </div>
        </div>
      </div>
    </div>

    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script defer src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script defer src="https://unpkg.com/bootstrap-table@1.18.1/dist/bootstrap-table.min.js"></script>
    <script defer src="js/app.js"></script>

  </body>
</html>

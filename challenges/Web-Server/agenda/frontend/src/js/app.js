var conferencesList;
var conference;

$( document ).ready(function() {

  fetch('http://agenda-backend.phack.fr/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: "query {conferences {id, name, city, talks {id, title, summary, speakers {id, name, githubAccount, blog}}}}"}),
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(json) {

    $('#table-conferences').bootstrapTable({
      pagination: false,
      search: false,
      columns: [{
        field: 'id',
        title: 'ID'
      },
      {
        field: 'name',
        title: 'Conférence'
      }, {
        field: 'city',
        title: 'Ville'
      },
      {
        field: 'id',
        title: ''
      }],
      data: json.data.conferences
    });

    conferencesList = json.data.conferences;

    $( "#table-conferences tr" ).each(function() {
      var lastTd = $(this).find("td:last");
      var id = $(lastTd).text();
      $(lastTd).empty();
      var r= $('<div class="showButton seeConf" data-conf-id=' + id +'><a href="#"><p><span class="bg"></span><span class="base"></span><span class="text">Voir</span></p></a></div>');
      $(lastTd).append(r);
    });

    $( "#table-conferences .seeConf" ).click(function() {
      showConferenceTalks(this);
    });
  });
});


function showConferenceTalks(element) {

  var id = $(element).data('conf-id');
  conference = conferencesList.filter(function (item){return item.id == id});

  $('#table-talks').bootstrapTable('destroy');
  $('#table-talks').bootstrapTable({
  pagination: false,
  search: false,
    columns: [{
      field: 'id',
      title: 'ID'
    },
    {
      field: 'title',
      title: 'Titre'
    }, {
      field: 'summary',
      title: 'Résumé'
    },
    {
      field: 'id',
      title: 'Animateurs'
    }],
    data: conference[0].talks
  });


  $( "#table-talks tr" ).each(function() {
    var lastTd = $(this).find("td:last");
    var id = $(lastTd).text();
    $(lastTd).empty();

    var r= $('<div class="showButton seeSpeaker" data-talk-id=' + id +'><a href="#"><p><span class="bg"></span><span class="base"></span><span class="text">Voir</span></p></a></div>');
    $(lastTd).append(r);
  });

  $( "#table-talks .seeSpeaker" ).click(function() {
    showTalkSpeaker(this);
  });


  $( "#confName").text("Conférence : " + conference[0].name);

  $('#table-talks').show();
  $('#subTalks').show();
  $("#confName").show();


  $([document.documentElement, document.body]).animate({
      scrollTop: $("#table-talks").offset().top
  }, 2000);
}


function showTalkSpeaker(element) {
  var id = $(element).data('talk-id');
  var talk = conference[0].talks.filter(function (item){return item.id == id});
  var speaker = talk[0].speakers[0];

  $('#profileName').text("Nom : " + speaker.name);
  $('#profileGithub').text("Github : " + speaker.githubAccount);
  $('#profileBlog').text("Blog : " + speaker.blog);

  $('#speakerModal').modal('show');
}

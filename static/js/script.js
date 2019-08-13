var url_cambridge = "https://dictionary.cambridge.org/es/buscar/english/direct/?q="

$.get('/api/attempts/', function(data){
    $('#words').DataTable({
        "data": data,
        "columns": [
          {"data": "word",
           'render': function (data, type, row, meta) {
                return meta.row + meta.settings._iDisplayStart + 1;
            }
          },
          { "data": "word_name",
            "render": function(data, type, row, meta){
             if(type === 'display'){
                    data = '<a onclick="showFrame()" target="cambridge-frame" href="' + url_cambridge + data + '">' + data + '</a>';
                }
                return data;
             }
          },
          { "data": "attempts" },
          { "data": "hits" },
          { "data": "accuracy",
            "render": function(data, type, row, meta){
             if(type === 'display'){
                    data = parseFloat(data).toFixed(1)+"%";
                }
                return data;
             }
          }
        ]
    });
});

function showFrame(){
    $('#cambridge-frame').show();
}

// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI
function AppViewModel() {

    var self = this;

    self.searchWord = function(data){
        var word_to_find = $('#word-to-find').val()
        showFrame();
        $('#cambridge-frame').attr('src',url_cambridge+word_to_find);
    }

     self.hideDictionary = function(){
        $('#cambridge-frame').hide()
    }

    self.addNewWord = function(){
        var word_to_add = $('#word-to-find').val()
        $.post( "/api/words/", {'name': word_to_add},function(data){
            console.log(data);
        });
    }

}

// Activates knockout.js
ko.applyBindings(new AppViewModel());
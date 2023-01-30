$(document).ready(function() {
    var table = $('#resortTable').DataTable( {
        scrollX: true,
        scrollCollapse: true,
        paging: true,
        'fixedColumns'  :   {
          leftColumns: 1,
        },
        dom: 'Qlfrtip',
        searchBuilder: {
            columns: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        }
    });
    
    $('ul').on('click', 'a', function() {

        if ($(this).text() == "Ikon & Colorado") {
            table
            .columns(13)
            .search("Ikon")
            .columns(14)
            .search("Colorado")
            .draw();
        } else if ($(this).text() == "Epic & Colorado") {
            table
            .columns(13)
            .search("Epic")
            .columns(14)
            .search("Colorado")
            .draw()
        } 
    });
});

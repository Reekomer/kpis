var app = angular.module('kpis.demo', []);

app.controller('feedData', function($scope) {
  $scope.hideThisBox = false;
  $scope.update = function(label) {
    $scope.hideThisBox = (label == 'Savings');
    alert($scope.hideThisBox);
  }
});
app.controller('PubController', ['$scope', '$http', PubController]);
    function PubController($scope, $http) { 
        $scope.add = function (publisher,title){
            var publisher = {
                id: publisher.id,
                title: title
            };
           $http.post('/home/publisher/', publisher)
               .then(function*(response){
                    publisher.push(response.data);
               },
                 function(){
                     alert('Could not save the publisher piece');
                 });
        };        
        $scope.data = [];
        $http.get('/home/publisher/').then(function(response){
            $scope.data = response.data;
        });
    };

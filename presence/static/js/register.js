var app = angular.module('register', ['ngSanitize','ui.select'])
    .config(function ($interpolateProvider, $httpProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
    .controller('MainController', function ($scope, $http, $timeout) {
        $scope.selected = null; // default value to prevent a match

        function getCourses(){
            $http.get("/api/courses?format=json",{})
            .success(function(response) {
                $scope.courses = response;
                restoreFormPresence();
            })
            .error(function(response){

            })
        }

        $scope.setCourse = function(id, index){
            $scope.selected = index;
            $scope.presence.course = $scope.courses[index].id
        }

        $scope.refreshStudents = function(){
            $http.get("/api/students?format=json",{})
            .success(function(response) {
                $scope.students = response;
            })
            .error(function(response){
                
            })
        }

        $scope.submitRegister = function(isValid) {

            // check to make sure the form is completely valid
            if (isValid) {
                $http.post("/api/students",$scope.user)
                .success(function(response) {
                    $scope.refreshStudents();
                    $scope.successUser = true;
                    $scope.errorUser = false;
                    $timeout(restoreFormUser,3000)
                })
                .error(function(response){
                    $scope.errorUser = true;
                    $timeout(restoreFormUser,5000)
                })
            }

          };
        
        $scope.submitPresence = function(isValid) {

            // check to make sure the form is completely valid
            if (isValid) {
                $scope.presence.student = $scope.presence.student.id;
                $http.post("/api/presences", $scope.presence)
                .success(function(response) {
                    $scope.refreshStudents();
                    $scope.successP = true;
                    $scope.errorP = false;
                    $timeout(restoreFormPresence,3000)
                })
                .error(function(response){
                    $scope.errorP = true;
                    $timeout(restoreFormPresence,5000)
                })
            }

          };
        
        function restoreFormPresence(){
            $scope.successP = false;
            $scope.errorP = false;
            $scope.presence = {};
            $scope.selected = null;
        };
        
        function restoreFormUser(){
            $scope.user = {};
            $scope.user.cursus="B1-IRCI";
            $scope.successUser = false;
            $scope.errorUser = false;
        };

        $scope.students=[];
        getCourses();
        restoreFormUser();
        restoreFormPresence();
        
    })
    .filter('propsFilter', function() {
        return function(items, props) {
            var out = [];

            if (angular.isArray(items)) {
                var keys = Object.keys(props);

                items.forEach(function(item) {
                    var itemMatches = false;

                    for (var i = 0; i < keys.length; i++) {
                        var prop = keys[i];
                        var text = props[prop].toLowerCase();
                        if (item[prop].toString().toLowerCase().indexOf(text) !== -1) {
                            itemMatches = true;
                            break;
                        }
                    }

                    if (itemMatches) {
                        out.push(item);
                    }
                });
            } else {
                // Let the output be the input untouched
                out = items;
            }

            return out;
        };
    })




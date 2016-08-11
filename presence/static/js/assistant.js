var app = angular.module('assistant', ['ngSanitize','ui.select'])
    .config(function ($interpolateProvider, $httpProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
    .controller('AssistantController', function ($scope, $http, $timeout, $interval) {
        
        $scope.delete = [];
        $scope.wipe = [];
        $scope.nobody = [];
        
        function getClassRooms(){
            $http.get("/api/classroom?format=json",{})
            .success(function(response) {
                $scope.classrooms = response;
                getQueues();
            })
            .error(function(response){

            })
        }

        function getCourses(){
            $http.get("/api/courses?format=json",{})
            .success(function(response) {
                $scope.courses = response;
            })
            .error(function(response){

            })
        }
        
        function getQueues(){
            for(i in $scope.classrooms){
                att_questions(i);
            }
        }

        function att_questions(i){
            $http.get('/api/queue/' + $scope.classrooms[i].id + '?format=json', {})
            .success(function(response) {
                $scope.questions[i] = response;
            })

        }
        
        $scope.submitWipe = function(isValid) {
            // check to make sure the form is completely valid
            if (isValid) {
                $http.delete("/api/queue/"+$scope.wipe[0],{})
                .success(function(response) {
                    getQueues();
                })
                .error(function(response){

                })
            }

        };

        $scope.submitNobody = function(isvalid) {
            // check to make sure the form is completely valid
            if (isvalid) {
                var payload = {'student': 1, 'course': $scope.nobody[0]}
                $http.post("/api/presences", payload)
                .success(function(response) {

                })
                .error(function(response){

                })
            }

        };
        
        $scope.submitForm = function(index) {
            // check to make sure the form is completely valid
            if (delete[index]) {
                $http.delete("/api/questions/"+$scope.delete[index],{})
                .success(function(response) {
                    getQueues();
                })
                .error(function(response){

                })
            }

        };

        getCourses();
        getClassRooms();
        $scope.questions = [];
        
    });

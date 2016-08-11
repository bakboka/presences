var app = angular.module('queue', ['ngSanitize','ui.select'])
    .config(function ($interpolateProvider, $httpProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
    .controller('QueueController', function ($scope, $http, $timeout, $interval) {
        
        $scope.question = {};

        function getClassRooms(){
            $http.get("/api/classroom?format=json",{})
            .success(function(response) {
                $scope.classrooms = response;
                getQueues();
                $interval(getQueues, 30000); // every 30sec
            })
            .error(function(response){

            })
        }
        
        function getStudents(){
            $http.get("/api/students?format=json",{})
            .success(function(response) {
                $scope.students = response;
            })
            .error(function(response){

            })
        }
        
        $scope.submitQuestion = function(isValid) {
            // check to make sure the form is completely valid
            if (isValid) {
                $scope.question.student = $scope.question.student.first_name + ' ' + $scope.question.student.last_name
                $http.post("/api/questions",$scope.question)
                .success(function(response) {
                    $scope.success = true;
                    $scope.error = false;
                    $timeout(restoreFormUser,3000)
                })
                .error(function(response){
                    $scope.error = true;
                    $timeout(restoreFormUser,5000)
                })
            }

        };
        
        function restoreFormUser(){
            $scope.question = {}
            $scope.error = false;
            $scope.success = false;
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

        getClassRooms();
        getStudents();
        $scope.questions = [];
    });

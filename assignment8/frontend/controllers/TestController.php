<?php

namespace frontend\controllers;

use \yii\web\Controller;

class TestController extends Controller { 

    public function actionIndex(){
        $data = 'data test';
        return $this->render('index', [
            'vdata' => $data
        ]);

        /* $data = 'data test';
        return $this->render('index', [
            'data test' => $data
        ]); */
    }

    public function actionTest(){
        echo 'test';
        return $this->render('test');
    }

}
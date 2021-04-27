<?php

class Login {
    private static $salt = "7heF@c3b00x";

    private $user;
    private $pass;
    private $type;

    public function __construct($user, $pass, $type)
    {
        $this->user = $user;
        $this->pass = self::hash($pass);
        $this->type = $type;
    }

    private static function hash($pass) {
        return md5($pass . self::$salt);
    }

    public function login($user, $pass) {
        return ($user === $this->user && self::hash($pass) === $this->pass);
    }

    public function type() {
        return $this->type;
    }
}

class LoginDB {
    private static $database = array(
        "student" => array(),
        "press" => array(),
    );

    public static function register($user) {
        array_push(self::$database[ $user->type() ], $user);
    }

    public static function login($user, $pass, $type) {
        foreach(self::$database[ $type ] as $key => $entry) {
            if ($entry->login($user, $pass)) {
                return $key + 1;
            }
        }
        return false;
    }
}

LoginDB::register( new Login("demo",      "demo",               "press")); # Guessable
LoginDB::register( new Login("cnn",       "iiGmmSvKFjJr4dp6AU", "press")); # Uncrackable
LoginDB::register( new Login("nyt",       "jp3yncQTKogJCyP9KT", "press")); # Uncrackable
LoginDB::register( new Login("guardian",  "jpdkslmSkeoJCyP9oO", "press")); # Uncrackable
LoginDB::register( new Login("fox",       "jKslA54sSjdAjs",     "press")); # Uncrackable

LoginDB::register( new Login("mike.spen@harvard.edu",           "Mike94",                    "student")); # Crackable
LoginDB::register( new Login("laura00@aol.com",                 "XxlauraxX",                 "student")); # Crackable
LoginDB::register( new Login("kev.rgn@caramail.com",            "NarutoUzumaki",             "student")); # Crackable
LoginDB::register( new Login("rachel.west@fox-news.com",        "fox12345",                  "student")); # Crackable
LoginDB::register( new Login("mark.zuckerberg@thefaceboox.com", "AFckingHardP4ssT0CrackIMO", "student")); # Uncrackable

<?php

# USER CLASS

class User {

  public $id;

  public $name            = "";
  public $member_sine     = "";
  public $last_update     = "";
  public $school          = "";
  public $status          = "";
  public $sex             = "";
  public $birthday        = "";
  public $home_town       = "";
  public $high_school     = "";
  public $email           = "";
  public $screenname      = "";
  public $mobile          = "";
  public $website         = "";
  public $looking_for     = "";
  public $interested_in   = "";
  public $relationship    = "";
  public $political_view  = "";
  public $interests       = "";
  public $favourite_music = "";
  public $picture         = "";

  public $profile = array();

  public function __construct($id) {

    $this->id = (is_int($id) && $id > 0 && $id <= UserDB::size()) ? $id : 1;

    foreach ( UserDB::get($this->id) as $key => $value) {
      $profile[$key] = $value;
    };

    $this->name             = $profile[ "name" ];
    $this->member_since     = $profile[ "member_since" ];
    $this->last_update      = $profile[ "last_update" ];
    $this->school           = $profile[ "school" ];
    $this->status           = $profile[ "status" ];
    $this->sex              = $profile[ "sex" ];
    $this->birthday         = $profile[ "birthday" ];
    $this->home_town        = $profile[ "home_town" ];
    $this->high_school      = $profile[ "high_school" ];
    $this->email            = $profile[ "email" ];
    $this->screenname       = $profile[ "screenname" ];
    $this->mobile           = $profile[ "mobile" ];
    $this->looking_for      = $profile[ "looking_for" ];
    $this->interested_in    = $profile[ "interested_in" ];
    $this->relationship     = $profile[ "relationship" ];
    $this->political_view   = $profile[ "political_view" ];
    $this->interests        = $profile[ "interests" ];
    $this->favourite_music  = $profile[ "favourite_music" ];
    $this->picture          = $profile[ "picture" ];

  }

  public function get($key){
    return $this->profile[ $key ];
  }

}

# FAKE DATABASE

class UserDB {

    private static $db = array(

      array(
        "name"            => "Mike",
        "member_since"    => "04-04-2004",
        "last_update"     => "05-05-2005",
        "school"          => "Harvard",
        "status"          => "Student",
        "sex"             => "Male",
        "birthday"        => "14-05-1984",
        "home_town"       => "Cambridge",
        "high_school"     => "Broady",
        "email"           => "mike.spen@harvard.edu",
        "screenname"      => "mickey123",
        "mobile"          => "5551234",
        "looking_for"     => "Friendship",
        "interested_in"   => "Woman",
        "relaionship"     => "Single",
        "political_view"  => "Democrat",
        "interests"       => "Music, Linux kernel",
        "favourite_music" => "Hip Hop",
        "picture"         => "fad7521cdef1a.jpg"
      ),

      array(
        "name"            => "Laura",
        "member_since"    => "04-04-2004",
        "last_update"     => "05-05-2005",
        "school"          => "Harvard",
        "status"          => "Student",
        "sex"             => "Femal",
        "birthday"        => "14-05-1984",
        "home_town"       => "Chicago",
        "high_school"     => "Carnot",
        "email"           => "laura00@aol.com",
        "screenname"      => "lauraa",
        "mobile"          => "5531234",
        "looking_for"     => "Friendship",
        "interested_in"   => "Men",
        "relaionship"     => "In relationship",
        "political_view"  => "Democrat",
        "interests"       => "Traveling, Reading",
        "favourite_music" => "Rock, indie",
        "picture"         => "bcd3d4c0e5e15.jpg"
      ),
      
      array(
        "name"            => "Kevin",
        "member_since"    => "04-04-2004",
        "last_update"     => "05-05-2005",
        "school"          => "Harvard",
        "status"          => "Student",
        "sex"             => "Male",
        "birthday"        => "14-05-1984",
        "home_town"       => "Los Angeles",
        "high_school"     => "Konoha",
        "email"           => "kev.rgn@caramail.com",
        "screenname"      => "KevRgn",
        "mobile"          => "552594",
        "looking_for"     => "Friendship",
        "interested_in"   => "Woman",
        "relaionship"     => "In relationship",
        "political_view"  => "Democrat",
        "interests"       => "PHP, Naruto",
        "favourite_music" => "Rap music",
        "picture"         => "f130d29ea9a2b.jpg"
      ),

      array(
        "name"            => "Rachel",
        "member_since"    => "12-06-2004",
        "last_update"     => "24-12-2006",
        "school"          => "Harvard (Former student)",
        "status"          => "Working at Fox News",
        "sex"             => "Femal",
        "birthday"        => "24-01-1968",
        "home_town"       => "N.Y.C",
        "high_school"     => "Unknown",
        "email"           => "rachel.west@fox-news.com",
        "screenname"      => "RachelWest",
        "mobile"          => "Hidden",
        "looking_for"     => "Friendship",
        "interested_in"   => "Unknown",
        "relaionship"     => "Unknown",
        "political_view"  => "Republican",
        "interests"       => "Politic, TV Shows",
        "favourite_music" => "Jazz, Pop",
        "picture"         => "ab12ffe489b4c.jpg"
      ),
      
      array(
        "name"            => "Mark Zuckerberg",
        "member_since"    => "04-04-2004",
        "last_update"     => "05-05-2005",
        "school"          => "Harvard",
        "status"          => "Student",
        "sex"             => "Male",
        "birthday"        => "14-05-1984",
        "home_town"       => "San Francisco, CA",
        "high_school"     => "MIT",
        "email"           => "mark.zuckerberg@thefaceboox.com",
        "screenname"      => "zucky",
        "mobile"          => "Hidden",
        "looking_for"     => "Friendship",
        "interested_in"   => "Woman",
        "relationship"    => "Single",
        "political_view"  => "Liberal",
        "interests"       => "Coding, Hacking",
        "favourite_music" => "Hip Hop",
        "picture"         => "22d23c2b9d85e.jpg"
      )

    );

    # Get user by id
    public static function get($id) {
      return self::$db[ $id - 1 ];
    }

    public static function size() {
      return count( self::$db );
    }

}

?>

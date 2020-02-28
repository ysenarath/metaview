import Vue from 'vue';

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import QueryPage from "./QueryPage.vue";
import HomePage from "./HomePage.vue";

new Vue({
    el: '#appQuery',
    render: h => h(QueryPage)
});

new Vue({
    el: '#appHome',
    render: h => h(HomePage)
});
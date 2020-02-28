<template>
    <nav class="navbar navbar-expand-lg navbar-light site-header shadow-sm">
        <a class="navbar-brand" href="/">{{ title }}</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item" v-for="item in menuItems" v-bind:class="{ active: item.title === activeItem }">
                    <a class="nav-link" v-bind:href="item.url">{{ item.title }}</a>
                    <span class="sr-only" v-if="item.title === activeItem">(current)</span>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    export default {
        props: ['activeItem'],
        data: function () {
            return {
                title: 'KnowledgeNet',
                menuItems: [
                    {'title': 'Home', 'url': '/'},
                    {'title': 'Query', 'url': '/query'},
                ],
            }
        }
    };
</script>

<style>
    .site-header {
        background-color: rgba(255, 255, 255, 0);
        z-index: 100;
    }
</style>
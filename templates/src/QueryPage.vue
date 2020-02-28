<template>
    <div class="app">
        <app-nav v-bind:activeItem="'Query'"></app-nav>
        <app-view></app-view>
    </div>
</template>

<script>
    import AppNav from './components/AppNav.vue';
    import AppView from './components/AppView.vue';

    export default {
        components: {
            AppNav,
            AppView
        }
    };
</script>

<style>
    :root {
        --sidebar-width: 350px;
    }

    .app {
        height: 100%;
    }
</style>
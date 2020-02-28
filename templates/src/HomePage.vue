<template>
    <div class="app">
        <app-nav v-bind:activeItem="'Home'"></app-nav>
    </div>
</template>

<script>
    import AppNav from './components/AppNav.vue';

    export default {
        components: {
            AppNav,
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
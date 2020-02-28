<template>
    <div class="app-view">
        <app-sidebar></app-sidebar>
        <app-content></app-content>
    </div>
</template>

<script>
    import AppContent from './AppContent.vue';
    import AppSidebar from './AppSidebar.vue';

    export default {
        components: {
            AppContent,
            AppSidebar
        }
    };
</script>

<style>
    .app-view {
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        padding-top: 56px;
        display: flex;
    }
</style>
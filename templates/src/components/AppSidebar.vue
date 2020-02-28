<template>
    <div class="app-sidebar">
        <query-results-view></query-results-view>
    </div>
</template>

<script>
    import QueryResultsView from "./QueryResultsView.vue";

    export default {
        components: {QueryResultsView}
    }
</script>

<style>
    .app-sidebar {
        height: 100%;
        border-right: 1px solid lightgray;
    }

    @media (max-width: 992px) {
        .app-sidebar {
            display: None;
        }
    }

    @media (min-width: 992px) {
        .app-sidebar {
            max-width: var(--sidebar-width);
            min-width: var(--sidebar-width);
            visibility: visible;
        }
    }
</style>
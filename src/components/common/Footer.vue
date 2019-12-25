<template>
    <div id="footer">
        <nav class="level">
            <p class="level-item has-text-centered">
                <a class="link is-info">Home</a>
            </p>
            <p class="level-item has-text-centered">
                <a class="link is-info">Menu</a>
            </p>
            <p class="level-item has-text-centered">
                <a class="link is-info">Reservations</a>
            </p>
            <p class="level-item has-text-centered">
                <a class="link is-info">Contact</a>
            </p>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
    #footer {
        width: 100%;
        height: 110px;
        background: black;
        z-index: 25;
    }
</style>
<script setup>
/* eslint-disable */
import AppTopNav from '../components/AppTopNav.vue';
import AppHomeHero from '../components/AppHomeHero.vue';
import AppStartTrading from '../components/AppStartTrading.vue';
import AppHomeExperience from '../components/AppHomeExperience.vue';
import AppHomeBenefit from '../components/AppHomeBenefit.vue';
import AppHomeTestimonial from '../components/AppHomeTestimonial.vue';
import AppWhyUs from '../components/AppWhyUs.vue';
</script>

<template>
    <div class="relative w-full h-full min-h-full flex flex-col bg-slate-900">

        <!-- start of nav -->
        <nav class="absolute top-0 right-0 w-full">
            <AppTopNav />
        </nav>

        <header class="w-full h-full flex">
            <AppHomeHero />
        </header>

        <aside>
            <AppStartTrading />
        </aside>

        <section>
            <AppHomeExperience />
        </section>
        
        <aside>
            <AppHomeBenefit />
        </aside>

        <article>
            <AppHomeTestimonial />
        </article>

        <section>
            <AppWhyUs />
        </section>

    </div>
</template>
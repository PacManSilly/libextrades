<script setup>
/* eslint-disable */
import AppTopNav from '../components/AppTopNav.vue';
import AppHomeHero from '../components/AppHomeHero.vue';
import AppHomeStartTrading from '../components/AppHomeStartTrading.vue';
import AppHomeExperience from '../components/AppHomeExperience.vue';
import AppHomeBenefit from '../components/AppHomeBenefit.vue';
import AppHomeTestimonial from '../components/AppHomeTestimonial.vue';
import AppHomeWhyUs from '../components/AppHomeWhyUs.vue';
import AppHomePlans from '../components/AppHomePlans.vue';
import AppHomeFaqs from '../components/AppHomeFaqs.vue';
import AppHomeContactUs from '../components/AppHomeContactUs.vue';
import AppHomeFooter from '../components/AppHomeFooter.vue';
</script>

<template>
    <div class="relative w-full h-full min-h-full flex flex-col bg-slate-900 overflow-x-hidden">

        <!-- start of nav -->
        <nav class="absolute top-0 right-0 w-full">
            <AppTopNav />
        </nav>

        <header class="w-full h-full flex">
            <AppHomeHero />
        </header>

        <aside>
            <AppHomeStartTrading />
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
            <AppHomeWhyUs />
        </section>

        <article>
            <AppHomePlans />
        </article>

        <section>
            <AppHomeFaqs />
        </section>

        <section>
            <AppHomeContactUs />
        </section>

        <footer>
            <AppHomeFooter />
        </footer>

    </div>
</template>
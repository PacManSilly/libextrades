<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserInvestment } from '../stores/investment';
import btclogo from '../assets/images/btc.png';
import btc_qrcode from '../assets/images/btc_qrcode.jpg';
import AppCopyText from './AppCopyText.vue';
import IconCreditCard from './icons/IconCreditCard.vue';
import IconBitcoin from './icons/IconBitcoin.vue'
import IconCloseBig from './icons/IconCloseBig.vue';
import IconLongRight from './icons/IconLongRight.vue';
import IconSetting from './icons/IconSetting.vue';
import AppInvestmentCard from './AppInvestmentCard.vue';

// store
const store = useUserInvestment()

// data
const modal = ref(false)
const depositId = ref(1)
const investmentId = ref(null)

const tabs = [
    {id: 1, type: "Bitcoin"},
    {id: 2, type: "Bank"},
]

// computed
const activeInvestment = computed(() => {
    return store.investments.data.find((plan) => plan.id == investmentId.value)
})

const isEmpty = computed(() => {
    return store.investments.data.length == 0
})

// methods
const deposit = (id) => {
    investmentId.value = id
    modal.value = true
}

const toDate = (value) => {
    const dateDate = new Date(value).toDateString()
    const dateTime = new Date(value).toLocaleTimeString()

    return `${dateDate} ${dateTime}`
}

// methods
const toCurrency = (value) => {
    const currencyFormatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    });

    return currencyFormatter.format(value)
}

// created
store.getInvestments()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <!-- loading -->
            <div v-if="store.investments.loading" class="w-full h-full flex items-center justify-center">
                <IconSetting class="w-10 h-10 fill-slate-600 md:w-20 md:h-20" />
            </div>

            <!-- error -->
            <div v-else-if="store.investments.error" class="w-full h-full flex items-center justify-center">
                <span class="text-red-600 text-sm md:text-lg">{{store.investments.error}}</span>
            </div>

            <!-- empty state -->
            <div v-if="isEmpty" class="w-full h-full flex items-center justify-center">
                <div class="w-full h-60 p-4 flex flex-col gap-5 items-center justify-center border-2 border-dashed border-slate-700 rounded-lg bg-slate-800 md:h-72 md:w-7/12 lg:p-6 lg:w-1/2">
                    <IconCreditCard class="w-20 h-20 fill-slate-700" />
                    <p class="text-center text-slate-600 font-medium text-sm md:text-base">You have not made any deposit. Please click the link below to select an investment plan</p>
                    <div class="">
                        <RouterLink :to="{name: 'investmentplan'}" class="text-blue-500 text-sm hover:text-blue-600 md:text-base">Select Plan</RouterLink>
                    </div>
                </div>
            </div>

            <!-- success -->
            <div v-else class="w-full h-full flex items-start justify-center">
                <div class="w-full flex flex-col gap-5 p-8 bg-slate-800 rounded-lg">
                    <div class="flex flex-col justify-between md:flex-row">
                        <div class="flex flex-col gap-2">
                            <p class="text-slate-300 font-medium text-2xl md:text-3xl">My Investments</p>
                            <span class="text-sm font-normal text-slate-600">A list of all your current investments, both active and pending. please click on the pay now button on investments marked as pending.</span>
                        </div>
                        <div class="">
                            <RouterLink :to="{name: 'investmentplan'}" class="group inline-flex items-center gap-2">
                                <span class="text-blue-600 text-sm md:text-base">Investment</span>
                                <IconLongRight class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                            </RouterLink>
                        </div>
                    </div>

                    <!-- <div class="mt-5 flex flex-col gap-4 md:gap-2">
                        <AppInvestmentCard @pay-now="deposit(investment.id)" v-for="investment in store.investments.data" :key="investment.id" v-bind="investment" />
                    </div> -->

                    <div class="bg-slate-900 max-h-96 overflow-auto">
                        <table class="w-full table-auto border-collapse border-spacing-2 min-w-[20rem]">
                            <thead class="">
                                <tr class="text-slate-300">
                                    <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Plan</th>
                                    <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Amount invested</th>
                                    <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Status</th>
                                    <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Date created</th>
                                    <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Duration</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="investment in store.investments.data" :key="investment.id" class="border-b border-slate-800 text-center last:border-none">
                                    <td class="p-4 text-sm text-slate-500 md:text-base">{{ investment.plan }}</td>
                                    <td class="p-4 text-sm text-slate-500 md:text-base">{{ investment.amount }}</td>
                                    <td class="p-4 text-sm text-slate-500">
                                        <span :class="investment.status == 'Active' ? 'bg-green-600':'bg-yellow-600'" class="text-white inline-block px-2 py-1 rounded-md">{{ investment.status }}</span>
                                    </td>
                                    <td class="p-4 text-sm text-slate-500 md:text-base">{{ toDate(investment.created) }}</td>
                                    <td class="p-4 text-sm text-slate-500 md:text-base">{{ investment.days }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                </div>
            </div>


        </div>

        <!-- payment modal -->
        <teleport to="body">
            <transition
                enter-from-class="scale-0 opacity-0"
                enter-active-class="transition-all duration-150"
                leave-to-class="scale-0 opacity-0"
                leave-active-class="transition-all duration-150">
                <div v-if="modal" class="w-full h-full min-h-full fixed top-0 z-30 overflow-auto bg-slate-900/90 backdrop-blur-lg">

                    <div class="w-full h-full relative flex items-center justify-center">
                        
                        <!-- close button -->
                        <button @click.prevent="modal = false" type="button" class="absolute group top-5 left-5 p-2 rounded transition-all duration-150 hover:bg-slate-800">
                            <IconCloseBig class="w-10 h-10 fill-slate-400 group-hover:fill-slate-200" />
                        </button>
                        
                        
                        <div class="w-10/12 h-full flex flex-col gap-10 mt-20 items-center lg:w-1/2">

                            <div class="flex flex-col items-center gap-5">
                                <p class="text-sm text-white font-bol md:text-base">Please select a payment method</p>
                                <div class="flex gap-5 items-center">
                                    <button
                                        v-for="tab in tabs"
                                        :key="tab.id"
                                        @click.prevent="depositId = tab.id"
                                        :class="depositId == tab.id ? 'bg-slate-800 text-white':'bg-transparent text-slate-500'"
                                        class="px-2 py-1 border border-slate-500 rounded font-medium text-base transition-all duration-150 hover:bg-slate-800 hover:text-white md:text-lg md:px-4">
                                        {{tab.type}}
                                    </button>
                                </div>
                            </div>
                            

                            <!-- start of btc payment -->
                            <div v-if="depositId == 1"  class="w-full flex flex-col gap-10 py-10 border-2 border-dashed border-slate-700 rounded-md items-center">

                                <div>
                                    <IconBitcoin class="w-32 h-32 fill-slate-700" />
                                </div>

                                <div class="w-full flex flex-col gap-10 text-center md:w-10/12">
                                    <span class="text-slate-400 text-sm md:text-base">
                                        Transfer between <code class="text-white font-bold">{{activeInvestment.amount}}</code> worth of Bitcoin to the address below
                                        or scan the QRCode with your Crypto wallet app
                                    </span>

                                    <div class="flex flex-col items-center justify-center gap-10">
                                        
                                        <!-- start of coin address and copy button -->
                                        <AppCopyText position="1">
                                            <template #copy>Copy address</template>

                                            <template #text>bc1q5pqulc7vu8e45nlhkdym3cu5cvuapf7e89cujw</template>
                                        </AppCopyText>
                                        <!-- end of coin address and copy button -->

                                        <!-- start of coin qrcode -->
                                        <div>
                                            <img :src="btc_qrcode" class="w-40 h-40 md:h-60 md:w-60">
                                        </div>
                                        <!-- end of coin qrcode -->

                                        <div>
                                            <span class="text-slate-400 text-sm md:text-base">
                                                Your Investment will automatically begin when
                                                the system recieves at most two blockchain confirmations.
                                            </span>
                                        </div>

                                    </div>
                                </div>

                            </div>
                            <!-- end of btc payment -->

                            <!-- start of bank payment -->
                            <div v-if="depositId == 2"  class="w-full flex flex-col gap-10 py-10 border-2 border-dashed border-slate-700 rounded-md items-center">

                                <div>
                                    <IconCreditCard class="w-32 h-32 fill-slate-700" />
                                </div>

                                <div class="w-full flex flex-col gap-10 text-center md:w-10/12">
                                    <span class="text-slate-400 text-sm md:text-base">
                                        Transfer between <code class="text-white font-bold">{{activeInvestment.amount}}</code> to the bank account below
                                    </span>

                                    <div class="flex flex-col items-center justify-center gap-5">

                                        <div class="flex items-center justify-between gap-5">
                                            <span class="text-sm text-slate-500 md:text-base">Bank Name:</span>
                                            <div>
                                                <AppCopyText position="2">
                                                    <template #copy>Copy</template>
                                                    <template #text>Apple Bank</template>
                                                </AppCopyText>
                                            </div>
                                        </div>

                                        <div class="flex items-center justify-between gap-5">
                                            <span class="text-sm text-slate-500 md:text-base">Account Name:</span>
                                            <div>
                                                <AppCopyText position="2">
                                                    <template #copy>Copy</template>
                                                    <template #text>Esperanza S. Hortal</template>
                                                </AppCopyText>
                                            </div>
                                        </div>

                                        <div class="flex items-center justify-between gap-5">
                                            <span class="text-sm text-slate-500 md:text-base">Account Nunber:</span>
                                            <div>
                                                <AppCopyText position="2">
                                                    <template #copy>Copy</template>
                                                    <template #text>1534010275</template>
                                                </AppCopyText>
                                            </div>
                                        </div>

                                        <div class="flex items-center justify-between gap-5">
                                            <span class="text-sm text-slate-500 md:text-base">Routing Number:</span>
                                            <div>
                                                <AppCopyText position="2">
                                                    <template #copy>Copy</template>
                                                    <template #text>226070584</template>
                                                </AppCopyText>
                                            </div>
                                        </div>

                                        <div class="flex items-center justify-between gap-5">
                                            <span class="text-sm text-slate-500 md:text-base">Swift Code:</span>
                                            <div>
                                                <AppCopyText position="2">
                                                    <template #copy>Copy</template>
                                                    <template #text>APPAUS33</template>
                                                </AppCopyText>
                                            </div>
                                        </div>

                                        <div class="mt-5">
                                            <span class="text-slate-400 text-sm md:text-base">
                                                Your Investment will automatically begin when your deposit has been confirmed.
                                            </span>
                                        </div>

                                    </div>
                                </div>

                            </div>
                            <!-- end of bank payment -->
                            

                        </div>

                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>

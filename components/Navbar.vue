<script setup>
    import user_list from "../assets/json/users.json";
    let users = user_list["users"]
</script>

<template>
    <INavbar>
        <INavbarBrand to="/"><b>Poger Archives</b></INavbarBrand>
        <INavbarCollapsible>
            <INav>
                <INavItem to="/"> Home </INavItem>
                <INavItem to="/about"> About </INavItem>
                <IDropdown>
                    <INavItem stop-propagation>Stuwants</INavItem>
                    <template #body>
                        <div v-for="u in users">
                            <IDropdownItem :to="{ path: '/users/' + u.user}">{{u["user"]}}</IDropdownItem>
                        </div>
                    </template>
                </IDropdown>
                <INavItem to="/pogers"> Pogers </INavItem>
            </INav>
        </INavbarCollapsible>
    </INavbar>
</template>
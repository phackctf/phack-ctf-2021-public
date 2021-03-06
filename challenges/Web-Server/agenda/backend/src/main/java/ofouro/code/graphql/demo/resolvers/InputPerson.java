package ofouro.code.graphql.demo.resolvers;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import ofouro.code.graphql.demo.model.Person;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class InputPerson {

    private String name;
    private String blog;
    private String githubAccount;
    private String login;
    private String passw0rd;

    Person convert() {
        return convert(this);
    }

    public static Person convert(InputPerson person) {
        return person != null ? new Person(person.name, person.githubAccount, person.blog, person.login, person.passw0rd, null) : null;
    }
}

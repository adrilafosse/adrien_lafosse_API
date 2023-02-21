package adrien.com.isen.lafosse;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.quarkus.mongodb.panache.common.MongoEntity;
import org.bson.types.ObjectId;

@MongoEntity(collection = "patients")
public class PatientEntity {

    public ObjectId id;

    @JsonProperty
    public String name;

    @JsonProperty
    public String sex;

    @JsonProperty
    public Long socialSecurityNumber;

    public PatientEntity(String name, String sex, Long socialSecurityNumber) {
        this.name = name;
        this.sex = sex;
        this.socialSecurityNumber = socialSecurityNumber;
    }

    public PatientEntity(ObjectId id, String name, String sex, Long socialSecurityNumber) {
        this.id = id;
        this.name = name;
        this.sex = sex;
        this.socialSecurityNumber = socialSecurityNumber;
    }

    public PatientEntity() { }
}
